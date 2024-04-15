import logging
import scapy.all as scapy
from threading import Thread
from queue import Queue
import time

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class NetworkMonitor:
    def __init__(self, interface="eth0", timeout=60):
        self.interface = interface
        self.timeout = timeout
        self.queue = Queue()
        self.stop_sniff = False

    def packet_handler(self, packet):
        self.queue.put(packet)  # Put the packet in the queue for processing

    def start_sniffing(self):
        # Start sniffing in a separate thread to avoid blocking
        sniff_thread = Thread(target=self.sniff_packets)
        sniff_thread.start()
        return sniff_thread

    def sniff_packets(self):
        scapy.sniff(
            iface=self.interface,
            prn=self.packet_handler,
            store=False,
            timeout=self.timeout,
        )

    def stop_sniffing(self):
        self.stop_sniff = True
        logging.info("Stopping sniffing")

    def analyze_traffic(self):
        # This method could be enhanced to filter and analyze traffic more specifically
        packets = []
        while not self.queue.empty():
            packet = self.queue.get()
            packets.append(packet)
        return packets

    def run_monitor(self):
        self.stop_sniff = False
        sniff_thread = self.start_sniffing()
        start_time = time.time()

        while time.time() - start_time < self.timeout and not self.stop_sniff:
            time.sleep(1)

        self.stop_sniffing()
        sniff_thread.join()
        return self.analyze_traffic()
