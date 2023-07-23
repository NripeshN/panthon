import unittest
from src import dos_attack
import threading
import socket
import time


class DummyServer:
    def __init__(self, host="localhost", port=50000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.sock.settimeout(1.0)
        self.connections = []
        self.running = True

    def start(self):
        while self.running:
            try:
                conn, addr = self.sock.accept()
                self.connections.append(conn)
            except socket.timeout:
                continue

    def stop(self):
        self.running = False  # stop the server
        for conn in self.connections:
            conn.close()
        self.sock.close()

    def connection_count(self):
        return len(self.connections)


class TestDoSAttack(unittest.TestCase):
    def setUp(self):
        self.server = DummyServer()
        self.server_thread = threading.Thread(target=self.server.start)
        self.server_thread.start()

    def tearDown(self):
        self.server.stop()
        self.server_thread.join()

    def test_simulation(self):
        dos = dos_attack.DoSAttack("localhost", 50000, 5)  
        initial_connections = self.server.connection_count()
        dos.simulate_attack()
        time.sleep(2)
        dos.wait_for_threads()
        final_connections = self.server.connection_count()
        self.assertEqual(final_connections - initial_connections, 5)


if __name__ == "__main__":
    unittest.main()
