from panthon import MITMAttack

target_ip = "10.9.0.6"  # Target IP address (HostB)
gateway_ip = "10.9.0.5"  # Gateway IP address (Modify as per your network configuration)
interface = "eth0"  # Network interface used for the attack

# Create an instance of MITMAttack
attack = MITMAttack()

# Set the necessary attributes
attack.set_attributes(target_ip, gateway_ip, interface)

# Run the MITM attack
attack.run_attack()
