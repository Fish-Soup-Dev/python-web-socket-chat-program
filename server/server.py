import socketserver
import threading
import datetime

def server(HOST, PORT):
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = str(self.request.recv(1024), "utf-8")

        if (self.data.partition(' ')[2].strip() != "U"):
            f = open("C:/Users/andre/Desktop/Real/server/ChatLog.txt", "a")
            f.write(self.data)
            ct = datetime.datetime.now()
            print(self.data.strip(), "", ct)
            f.close()

        f = open("C:/Users/andre/Desktop/Real/server/ChatLog.txt", "r")
        self.request.sendall(bytes(f.read(), "utf-8"))
        f.close()
        
if __name__ == "__main__":
    localIP = input("system ip:")
    HOST, PORT = localIP, 9999
    serv1 = threading.Thread(target=server, args=(HOST, PORT,))
    serv1.start()
    HOST, PORT = localIP, 9998
    serv2 = threading.Thread(target=server, args=(HOST, PORT,))
    serv2.start()