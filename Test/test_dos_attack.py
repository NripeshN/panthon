import pytest
from unittest.mock import patch, Mock
from panthon.dos_attack import DoSAttack


def test_create_connection_success():
    with patch("panthon.dos_attack.socket.socket") as mock_socket:
        mock_socket_instance = Mock()
        mock_socket.return_value = mock_socket_instance

        dos = DoSAttack()
        dos.create_connection(url="http://localhost", target_port=8080)

        mock_socket_instance.connect.assert_called_once()
        mock_socket_instance.send.assert_called()
        mock_socket_instance.close.assert_called_once()


def test_create_connection_failure():
    with patch("panthon.dos_attack.socket.socket") as mock_socket:
        mock_socket_instance = Mock()
        mock_socket.return_value = mock_socket_instance
        mock_socket_instance.connect.side_effect = Exception("Mock Exception")

        dos = DoSAttack()
        dos.create_connection(url="http://localhost", target_port=8080)

        mock_socket_instance.close.assert_not_called()


def test_slowloris_attack_initial_connection():
    with patch("panthon.dos_attack.socket.socket") as mock_socket, patch(
        "panthon.dos_attack.read_user_agents", return_value=["UA1", "UA2"]
    ):
        mock_socket_instance = Mock()
        mock_socket.return_value = mock_socket_instance

        dos = DoSAttack()
        dos.slowloris_attack(
            url="http://localhost", target_port=8080, num_connections=2
        )

        mock_socket_instance.send.assert_called()
        assert mock_socket_instance.send.call_count == 2


# ... similarly for other methods ...


def test_goldeneye_attack():
    with patch("subprocess.run") as mock_subprocess:
        dos = DoSAttack()
        dos.goldeneye_attack(url="http://localhost")

        mock_subprocess.assert_called_once()
