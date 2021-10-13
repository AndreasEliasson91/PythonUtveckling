from communication.serversocket import ServerSocket
from game.player import Player


class Game:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connected_players = []

    def run(self):
        with ServerSocket(self.host, self.port) as server_socket:
            while True:
                client_socket, client_address = server_socket.accept()
                player = Player(client_socket)
                self.connected_players.append(player)

