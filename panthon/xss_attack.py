import requests
import logging
import os
import subprocess
from panthon.XSS.XSSCon.lib import core
from panthon.XSS.XSSCon.lib.crawler.crawler import *
from panthon.XSS.XSSCon.lib.helper.Log import *
import json

logging.basicConfig(level=logging.INFO)


class XSSAttack:
    def xanxxs_attack(
        self, url, time=25, file="panthon/XSS/XanXSS/xss-payload-list.txt", amount=1
    ):
        # path_to_executable = os.path.join(os.path.dirname(__file__), "panthon/XSS/XanXSS/xanxss.py")
        current_path = os.getcwd()
        print(current_path)

        path_to_executable = f"{current_path}/panthon/XSS/XanXSS/xanxss.py"
        # base_dir = os.path.dirname(os.path.realpath(__file__))
        # file_path = os.path.join(base_dir, "XSS", "XanXSS", "xss-payload-list.txt")
        # path_to_executable = os.path.join(base_dir, "XSS", "XanXSS", "xanxss.py")
        with open(file, "r") as f:
            payloads = [line.strip() for line in f]

        command = ["python3", path_to_executable, "-u", url, "--payloads"]
        command.extend(payloads)
        command.extend(["--time", str(time)])
        command.extend(["-a", str(amount)])
        print("xanxss")
        subprocess.run(command)

    def xsscon_attack(
        self,
        url,
        depth=2,
        payloadLevel=6,
        payload=None,
        userAgent="'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'",
        single=False,
        proxy=None,
        cookie=None,
        method=2,
    ):

        print("xsscon")
        path_to_executable = os.path.join(
            os.path.dirname(__file__), "XSS/XSSCon/xsscon.py"
        )

        cookies = cookie.split(";")
        cookie_dict = {}
        for c in cookies:
            key, value = c.split("=")
            cookie_dict[key.strip()] = value.strip()

        cookie_json = json.dumps(cookie_dict)
        print(cookie_json)

        command = [
            "python3",
            path_to_executable,
            "-u",
            str(url),
            "--depth",
            str(depth),
            "--payload-level",
            str(payloadLevel),
            "--payload" if payload else "",
            str(payload) if payload else "",
            "--user-agent",
            str(userAgent),
            "--single" if single else "",
            "--proxy" if proxy else "",
            str(proxy) if proxy else "",
            "--cookie" if cookie else "",
            str("'" + cookie_json + "'") if cookie else "",
            "--method",
            str(method),
        ]

        command_str = " ".join(command)
        subprocess.run(command_str, shell=True)
