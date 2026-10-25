# Server side of the TCP Socket
import socket

port = 12345

def server():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind(("localhost", port))
    my_socket.listen(5)
    print("Listening...")

    incoming_socket, incoming_address = my_socket.accept()

    data = incoming_socket.recv(1024).decode('utf-8')

    incoming_socket.sendall(data.upper().encode('utf-8'))

    incoming_socket.close()
    my_socket.close()

server()