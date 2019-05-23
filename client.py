#dozhi
#chat-me client side of program
#python3

import socket
from threading import Thread
import tkinter


'''GLOBALS'''
PORT = 65432
BUFSIZ = 1024 #we are setting incoming data size for 1kb

'''FOR TESTING REASON WE DO IT AT LOCAL LEVEL FOR THE START'''
local_address = socket.gethostbyname(socket.gethostname())


#Creating TCP/IP socket named as "client"
client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)



def recieve():
	"""Handles incoming data from server"""
	while True:
		try:
			msg = client.recv(BUFSIZ).decode("utf8")
			msg_list.insert(tkinter.END , msg)
		except OSerror: #error to catch if client has left chat
			break

def sending(event=None):
	"""Handles sending data to server"""
	msg= my_msg.get()
	my_msg.set("")
	client.send(bytes(msg, 	"utf8"))
	if msg == "{exitapp}":
		client.close()
		top.quit()


def on_exiting_app(event=None):
	"""For clear exiting and not to leave garbage"""
	my_msg.set("{exitapp}")
	sending()


window = tkinter.Tk()

window.title("Chat-me")
window.geometry("500x400")

messages_frame = tkinter.Frame(window)

my_msg = tkinter.StringVar() #used to get instace of input
my_msg.set("Type your messsage here...")

scrollbar = tkinter.Scrollbar(messages_frame) #navigation for old messages

msg_list = tkinter.Listbox(messages_frame , height= 20 , width= 60 , yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(window, textvariable=my_msg)
entry_field.bind("<Return>", sending)
entry_field.pack()
send_button = tkinter.Button(window, text="Send", command=sending)
send_button.pack()

window.protocol("WM_DELETE_WINDOW" , on_exiting_app)


try:
	client.connect((local_address , PORT))
except (NameError , ConnectionRefusedError):
	print("No server found")

get_thread = Thread(target=recieve)
get_thread.start()


window.mainloop()


#if __name__=="__main__":
