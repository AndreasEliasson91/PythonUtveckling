from communication.clientsocket import ClientSocket


class Player:
    def __init__(self, client_socket):
        self.client_socket = ClientSocket(client_socket)
        # TODO: Move this to thread
        self.username = self.client_socket.prompt("Enter your username: ")
        self.inventory = []
        # TODO: Start threads

    def send_thread(self):
        pass

    def receive_thread(self):
        pass
