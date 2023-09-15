from panthon import XSSAttack

url = "http://testphp.vulnweb.com"
xss_attack = XSSAttack(url)
forms = xss_attack.get_all_forms()
for form in forms:
    form_details = xss_attack.get_form_details(form)
    xss_attack.attack(form_details)
