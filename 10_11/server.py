import socket
import threading
import queue


HOST = '127.0.0.1'
PORT = 32195

message_queue = queue.Queue()
client_list = []


def broadcast_thread():
    while True:
        message_data = message_queue.get()
        sender_socket = message_data['client_socket']
        username = message_data['username']
        message = message_data['message']

        for client in client_list:
            if client != sender_socket:
                message_to_send = f'{username}: {message}'
                message_to_send = message_to_send.encode('utf-8')
                client.sendall(message_to_send)

        message_queue.task_done()


def client_thread(client_socket):
    client_socket.sendall(b'Enter chat name: ')
    username = client_socket.recv(1024).decode('utf-8')  # 1024 is the max byte value to receive

    while True:
        message = client_socket.recv(1024).decode('utf-8')

        if message.lower() == '!quit':
            client_list.remove(client_socket)

            data_dict = {
                'client_socket': client_socket,
                'username': username,
                'message': 'Has left the chat'
            }

            message_queue.put(data_dict)
            break
            
        data_dict = {
            'client_socket': client_socket,
            'username': username,
            'message': message
        }

        message_queue.put(data_dict)

    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET = IPv4, SOCK_STREAM = TCP
    server_socket.bind((HOST, PORT))  # Bind the socket to the address
    server_socket.listen()  # Enable server to accept connections

    threading.Thread(target=broadcast_thread).start()

    while True:
        # Blocking call - The program stops here until something happens
        client_socket, client_address = server_socket.accept()
        print(f"Got a connection from {client_address}")

        client_list.append(client_socket)

        thread = threading.Thread(target=client_thread, args=(client_socket,))
        thread.start()

    server_socket.close()


if __name__ == '__main__':
    main()
