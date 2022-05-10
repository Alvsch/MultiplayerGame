import pickle
import socket

HEADER = 16
FORMAT = "utf-8"

class Network:
	def __init__(self, conn: socket.socket, addr):
		self.conn = conn
		self.addr = addr

	def listen(self):
		msg_length = self.conn.recv(HEADER).decode(FORMAT)
		if msg_length:
			msg_length = int(msg_length)
			msg = pickle.loads(self.conn.recv(msg_length))
			return msg

	def send(self, msg):
		message = pickle.dumps(msg)
		msg_length = len(message)
		send_length = str(msg_length).encode(FORMAT)
		send_length += b" " * (HEADER - len(send_length))
		self.conn.send(send_length)
		self.conn.send(message)

	def send_and_wait(self, msg):
		self.send(msg)
		return self.listen()