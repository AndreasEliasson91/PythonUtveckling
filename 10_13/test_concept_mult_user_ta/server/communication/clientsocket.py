class ClientSocket:
    def __init__(self, socket):
        self.socket = socket

    def send(self, message):
        pass

    def receive(self):
        pass

    def prompt(self, prompt_message):
        self.socket.sendall(prompt_message.encode('utf-8'))
        return self.