import requests
import logging
import os
import subprocess
from panthon.XSS.XSSCon.lib import core
from panthon.XSS.XSSCon.lib.crawler.crawler import *
from random import randint
from panthon.XSS.XSSCon.lib.helper.Log import *

logging.basicConfig(level=logging.INFO)


class XSSAttack:
    def xanxxs_attack(self, url, time=25, file="panthon/XSS/XanXSS/xss-payload-list.txt", amount=1):
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

    def xsstrike_attack(self, url, threads=1000, file="panthon/XSS/XSStrike/xsstrike.py"):
        path_to_executable = os.path.join(
            os.path.dirname(__file__), "XSS/XSStrike/xsstrike.py"
        )

        command = [
            "python3",
            path_to_executable,
            "-u",
            url,
            "-t",
            str(threads),
            # "--file",
            # file,
        ]

        subprocess.run(command)

    def xsscon_attack(
        self,
        url,
        depth=2,
        payloadLevel=6,
        payload=None,
        userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        single=False,
        proxy=None,
        cookie="""{"ID":"1094200543"}""",
        method=2,
    ):
        def check(payloadLevel, payload):
            payload = int(payloadLevel)
            if payload > 6 and payload is None:
                payload = core.generate(randint(1, 6))
            else:
                payload = core.generate(payload)
            print(payload)
            return payload if payload is None else payload

        print("xsscon")
        headers = {"User-Agent": userAgent}
        calculated_payload = check(payloadLevel, payload)

        if url:
            core.main(url, proxy, headers, calculated_payload, cookie, method)
            crawler.crawl(
                url, depth, proxy, userAgent, calculated_payload, method, cookie
            )
        elif single:
            core.main(single, proxy, headers, calculated_payload, cookie, method)

