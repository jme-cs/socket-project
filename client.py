# Creating a client-server connection using socket

import socket

ip = input("IP address: ").strip()

port = int(input("Port: "))

def client():

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((ip, port))

    message = input("Enter a Message: ")

    my_socket.send(message.encode('utf-8'))
    server_response = my_socket.recv(1024)

    print(server_response.decode('utf-8'))

    my_socket.close()

client()