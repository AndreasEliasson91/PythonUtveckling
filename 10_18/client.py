import socket
import threading

HOST = '127.0.0.1'
PORT = 32195

running = True


def sender(client_socket):
    global running
    while running:
        message = input()
        if message.lower() == '!quit':
            running = False
        message = message.encode('utf-8')
        client_socket.sendall(message)


def receiver(client_socket):
    while running:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    welcome_message = client_socket.recv(1024).decode('utf-8')
    print(welcome_message)

    quote = client_socket.recv(1024).decode('utf-8')
    print(quote)

    name_question = client_socket.recv(1024).decode('utf-8')
    name = bytes(input(name_question), 'utf-8')
    client_socket.sendall(name)

    sender_thread = threading.Thread(target=sender, args=(client_socket,))
    receiver_thread = threading.Thread(target=receiver, args=(client_socket,))

    sender_thread.start()
    receiver_thread.start()

    sender_thread.join()
    receiver_thread.join()

    client_socket.close()


if __name__ == '__main__':
    main()
