from panthon import XSSAttack

url = "http://localhost:3000/#/complain"
# url = "'http://localhost:4280/vulnerabilities/xss_s/'"
# cookie = "PHPSESSID=4142188189348f284c16ff843f25df7a;security=low"

xss_attack = XSSAttack()
xss_attack.xanxxs_attack(url=url)
