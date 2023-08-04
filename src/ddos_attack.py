import torch
import torch.nn as nn
import threading
from .random_string_generator import RandomStringGenerator
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DDoSAttack:
    def __init__(
        self, target_ip, target_port, num_connections, attack_type="aSYNcrone"
    ):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.attack_type = attack_type
        self.threads = []
        self.model = RandomStringGenerator()

    def create_connection(self):
        for _ in range(self.num_connections):
            thread = threading.Thread(target=self.run_attack)
            self.threads.append(thread)
            thread.start()

    def run_attack(self):
        if self.attack_type == "aSYNcrone":
            self.aSYNcrone_attack()
        elif self.attack_type == "slowloris":
            self.slowloris_attack()
        else:
            logging.error(f"Unknown attack type: {self.attack_type}")

    def aSYNcrone_attack(self):
        # TODO: Implement the aSYNcrone attack here
        raise NotImplementedError

    def slowloris_attack(self):
        # TODO: Implement the Slowloris attack here
        raise NotImplementedError

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


class BotNet:
    def __init__(
        self, num_bots, target_ip, target_port, num_connections, attack_type="aSYNcrone"
    ):
        self.num_bots = num_bots
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.attack_type = attack_type
        self.bots = []

    def create_bots(self):
        for _ in range(self.num_bots):
            bot = DDoSAttack(
                self.target_ip, self.target_port, self.num_connections, self.attack_type
            )
            self.bots.append(bot)

    def launch_attack(self):
        for bot in self.bots:
            bot.create_connection()
        for bot in self.bots:
            bot.wait_for_threads()
