import requests
from bs4 import BeautifulSoup
import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)


class XSSAttack:
    def __init__(
        self,
        url,
        time=25,
        checks=5,
        threads=1,
        attack_type="xanxxs",
        file="XanXSS/xss-payload-list.txt",
    ):
        self.url = url
        self.time = time
        self.file = file
        self.session = requests.Session()
        with open(self.file, "r") as file:
            self.payloads = [line.strip() for line in file]
        self.threads = []
        self.threads = threads
        self.attack_type = attack_type

    def create_attacks(self):
        self.run_attack()

    def run_attack(self):
        if self.attack_type == "xanxxs":
            self.xanxxs_attack()
        if self.attack_type == "xsstrike":
            self.xsstrike_attack()
        else:
            logging.error(f"Unknown attack type: {self.attack_type}")

    def xanxxs_attack(self):
        path_to_executable = os.path.join(os.path.dirname(__file__), "XanXSS/xanxss.py")
        command = ["python3", path_to_executable, "-u", self.url, "--payloads"]
        command.extend(self.payloads)
        command.extend(["--time", str(self.time)])
        command.extend(["-a", "1"])

        subprocess.run(command)

    def xsstrike_attack(self):
        path_to_executable = os.path.join(
            os.path.dirname(__file__), "XSStrike/xsstrike.py"
        )
        command = [
            "python3",
            path_to_executable,
            "-u",
            self.url,
            "-t",
            str(self.threads),
            "--file",
            self.file,
        ]

        subprocess.run(command)

    def xspear_attack(self):
        command = [
            "xspear",
            "-u",
            self.url,
            "-t",
            str(self.threads),
            "-o",
            "json",
        ]
        subprocess.run(command)


# Target URL
target_url = "http://xss-game.appspot.com/level1/frame?query="

# Create and launch attack
attack = XSSAttack(target_url, time=25, checks=5, threads=100, attack_type="xsstrike")
attack.create_attacks()
attack.wait_for_threads()
