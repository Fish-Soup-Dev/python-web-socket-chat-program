import socket
import os

def SendString(HOST, PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(bytes(name + ": " + data + "\n", "utf-8"))
        ReceivedData = str(sock.recv(1024), "utf-8")
        os.system('cls' if os.name == 'nt' else 'clear')
        print("{}".format(ReceivedData))

if __name__ == '__main__':
    HOST = input("IP Adress:")
    PORT = int(input("Port Number:"))
    name = input("name: ")

    while (1 == 1):
        data = input("> ")
        SendString(HOST, PORT)