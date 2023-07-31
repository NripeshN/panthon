from src import SQLInjectionAttack

url = "http://testphp.vulnweb.com/?id=1"
sql_injection_attack = SQLInjectionAttack(url)
sql_injection_attack.attack()
