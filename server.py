import socket
from network import Network
import threading
from game import *

IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

game = Game()
connections = 0

def handle_client(n: Network):
	global game, connections
	print(f"Client Connected From Address {n.addr}")

	p = Player(str(connections), color=(255, 0, 0))
	game.addPlayer(p)
	n.send(p)
	while True:
		try:
			n.send(game)
			p = n.listen()
			game.updatePlayer(p)
		except:
			break
	print(f"Connected Lost: {ADDR}")
	n.conn.close()



server.listen()
print(f"Server Hosting At IP: {IP}, On Port: {PORT}")

while True:
	try:
		conn, addr = server.accept()
		n = Network(conn ,addr)
		connections += 1

		thread = threading.Thread(target=handle_client, args=(n,))
		thread.start()

	except KeyboardInterrupt:
		print("Server Closed")
		server.close()
		exit()