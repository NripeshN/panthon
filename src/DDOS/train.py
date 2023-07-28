import torch
import torch.nn as nn
import torch.optim as optim

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


def train_model():
    input_dim = 100
    hidden_dim = 512
    output_dim = 100
    n_layers = 2

    model = LSTMGenerator(input_dim, hidden_dim, output_dim, n_layers)

    # Assume we are on a CUDA machine, then this should print a CUDA device:
    if torch.cuda.is_available():
        device = torch.device('cuda')
    elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        device = torch.device('mps')
    else:
        device = torch.device('cpu')

    # transfer the model to device
    model = model.to(device)

    # loss and optimizer
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters())

    # training data placeholder, replace with your data
    data = torch.randn((1000, 100, 100))

    for epoch in range(100):  # number of epochs
        for sequence in data:
            sequence = sequence.to(device)
            # Forward pass
            outputs = model(sequence.unsqueeze(0))
            loss = criterion(outputs, sequence.unsqueeze(0))

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f'Epoch {epoch+1}/{100}, Loss: {loss.item()}')

    # Save the trained model
    torch.save(model.state_dict(), "model.pth")
    print("Model trained and saved as model.pth")


if __name__ == "__main__":
    train_model()
