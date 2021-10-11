import socket

HOST = '127.0.0.1'
PORT = 32195


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    name_question = client_socket.recv(1024).decode('utf-8')
    name = bytes(input(name_question), 'utf-8')
    client_socket.sendall(name)

    while True:
        out_message = input('>> ')
        out_message = out_message.encode('utf-8')
        client_socket.sendall(out_message)

        in_message = client_socket.recv(1024).decode('utf-8')
        print(in_message)

    client_socket.close()


if __name__ == '__main__':
    main()
