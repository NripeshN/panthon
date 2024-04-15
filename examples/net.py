from panthon import NetworkMonitor

monitor = NetworkMonitor(interface="eth0", timeout=1)
packets = monitor.run_monitor()
print(packets)