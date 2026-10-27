# Server side of the TCP Socket

import socket

port = 12345

def server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(("localhost", port))
    my_socket.listen(5)
    print(f"Listening from port {port} ...")

    incoming_socket, incoming_address = my_socket.accept()
    print(f"Connected from: {incoming_address[0]} : {incoming_address[1]}")

    while True:
        data = incoming_socket.recv(1024).decode('utf-8')

        if not data:
            print("Client disconnected")
            break

        incoming_socket.sendall(data.upper().encode('utf-8'))

    incoming_socket.close()
    my_socket.close()

server()
#'b"hello"'