#dozhi
#chat-me server part 
#python3 

import socket
from threading import Thread

'''GLOBALS'''
PORT = 65432 #basic port
BUFSIZ = 1024 #Setting pref size of inc req to 256Bytes

clients = {} #list of user clients
clients_addresses = {}#list of user clients' addresses


#creating TCP/IP pot
SERVER = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

#Getting server host address
server_address = socket.gethostbyname(socket.gethostname())

ADDR = (server_address , PORT)

SERVER.bind(ADDR)#binding ip addr and port as addr to socket



def incoming_connection_controller():
	'''Controlling incoming clients coonections'''
	while True:
		client , client_address = SERVER.accept()
		print("%s : has connected to server!" % client)


if __name__ == "__main__":
	print("Server is starting...")
	SERVER.listen(2)#setting to server listen for 2 incoming req
	ACCEPT_THREAD = Thread(target=incoming_connection_controller)#Setting thread of inc req controller to obj by creating obj
	ACCEPT_THREAD.start()
	ACCEPT_THREAD.join()