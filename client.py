# Creating a client-server connection using socket

import socket

def client(ip, port):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((ip, port))

    try:
        while True:
            message = input("Enter a Message ('q' to Quit): ").strip()
            if message == "q":
                break
            if message == "":
                print("Error: Message cannot be empty")
                continue

            my_socket.sendall(message.encode('utf-8'))
            server_response = my_socket.recv(1024)
            print(server_response.decode('utf-8'))
    finally:
        print("Closing socket...")
        my_socket.close()

def main():
    ip = input("Server IP Address: ").strip()
    while True:
        try:
            port = int(input("Server Port: "))
            break
        except ValueError:
            print("Error: Port must be an integer")

    client(ip, port)

main()