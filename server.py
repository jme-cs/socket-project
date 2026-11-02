# Server side of the TCP Socket

import socket

host = input("Enter an IP address (ex 'localhost'): ")

while True:
    try:
        port = int(input("Enter a port number (ex '8080'): "))
        break
    except ValueError:
        print("Port number must be an integer")


def server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen(1)
    print(f"Listening from port {port} ...")

    my_socket.settimeout(5)

    try:
        incoming_socket, incoming_address = my_socket.accept()
        print(f"Connected from: {incoming_address[0]} : {incoming_address[1]}")
    except socket.timeout:
        print("Socket timed out")
        my_socket.close()
        return

    try:
        while True:
            data = incoming_socket.recv(1024).decode('utf-8')
            if not data:
                break
            incoming_socket.sendall(data.upper().encode('utf-8'))
    finally:
        print("Client disconnected")
        incoming_socket.close()
        my_socket.close()

server()