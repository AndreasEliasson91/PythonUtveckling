import socket


class ServerSocket:
    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))

    def __enter__(self):
        self.socket.listen()
        return self.socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()
