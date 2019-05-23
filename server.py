#dozhi
#chat-me
#simple server and client chat program to remember threads and socket.
#1/2 program

from socket import AF_INET , socket , SOCK_STREAM
from threading import Thread


'''GLOBAL CONSTANTS'''
clients = {}
adresses = {}

HOST = "" #empty var to be filled with host name or ip adress
PORT = 33000 # port to work with
BUFSIZ = 1024
ADDR = (HOST , PORT)
SERVER = socket(AF_INET , SOCK_STREAM)
SERVER.bind(ADDR)



def accept_incoming_connections():
	while True:
		client , client_adress = SERVER.accept()
		print("%s:%s has connected!")
		client.send("Your are connected...\n "+"Type your nickname and press enter to continue " , "utf8")
		adress[client] = client_adress
		thread(target=handle_client , args=(client,)).start()


def handle_client(client):  # Takes client socket as argument.
    """Handles a single client connection."""
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    broadcast(bytes(msg, "utf8"))
    clients[client] = name
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            broadcast(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)








if __name__=="__main__":
    SERVER.listen(5)  # Listens for 5 connections at max.
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    SERVER.close()
