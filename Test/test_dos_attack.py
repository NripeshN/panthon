import unittest
from src import dos_attack
import threading
import socket


class DummyServer:
    def __init__(self, host="localhost", port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.connections = []

    def start(self):
        while True:
            conn, addr = self.sock.accept()
            self.connections.append(conn)

    def stop(self):
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
        dos = dos_attack.DoSAttack(
            "localhost", 9999, 5
        )  # target localhost, port 9999, 5 connections
        initial_connections = self.server.connection_count()
        dos.simulate_attack()
        dos.wait_for_threads()
        final_connections = self.server.connection_count()
        self.assertEqual(final_connections - initial_connections, 5)


if __name__ == "__main__":
    unittest.main()
