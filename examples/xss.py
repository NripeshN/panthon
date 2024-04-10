from panthon import XSSAttack

url = "http://localhost:3000/#/complain"

xss_attack = XSSAttack.xsscon_attack(self=XSSAttack,url=url)

# forms = xss_attack.get_all_forms()
# for form in forms:
#     form_details = xss_attack.get_form_details(form)
#     xss_attack.attack(form_details)
