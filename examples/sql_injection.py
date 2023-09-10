from panthon import SQLInjectionAttack

# Example usage:
sql_injection_attack = SQLInjectionAttack()
target_url = "http://localhost:3000/rest/products/search?q="
sql_injection_attack.sqli_scanner(target_url)
sql_injection_attack.sqlmap_attack(target_url)
