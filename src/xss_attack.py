import requests
import logging
import os
import subprocess

logging.basicConfig(level=logging.INFO)


class XSSAttack:
    def xanxxs_attack(self, url, time=25, file="XanXSS/xss-payload-list.txt", amount=1):
        path_to_executable = os.path.join(os.path.dirname(__file__), "XanXSS/xanxss.py")
        with open(file, "r") as f:
            payloads = [line.strip() for line in f]

        command = ["python3", path_to_executable, "-u", url, "--payloads"]
        command.extend(payloads)
        command.extend(["--time", str(time)])
        command.extend(["-a", str(amount)])

        subprocess.run(command)

    def xsstrike_attack(self, url, threads=1000, file="XSStrike/xsstrike.py"):
        path_to_executable = os.path.join(
            os.path.dirname(__file__), "XSStrike/xsstrike.py"
        )

        command = [
            "python3",
            path_to_executable,
            "-u",
            url,
            "-t",
            str(threads),
            "--file",
            file,
        ]

        subprocess.run(command)


# Target URL
target_url = "http://localhost:3000/#/search?q="

# Create and launch xanxxs attack
attack = XSSAttack()
attack.xanxxs_attack(target_url, time=25, file="XanXSS/xss-payload-list.txt")

# Create and launch xsstrike attack
attack.xsstrike_attack(target_url, threads=1000, file="XSStrike/xsstrike.py")
