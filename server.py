import socket
import threading

from game import *
from network import *

IP = socket.gethostbyname(socket.gethostname())

PORT = 5050
ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = 0
game = Game()

def handle_client(net: Network):
	global game, connections
	print(f"New Connection From {network.getAddress()}")

	connections += 1

	net.send(Player(f"player{str(connections)}", 50, 50))
	while True:
		network.send(game)
		p = network.listen()
		game.updatePlayer(p)


server.listen()
print(f"Started Server On IP: {IP} and PORT: {PORT}")

while True:
	conn, addr = server.accept()
	network = Network(conn, addr)

	thread = threading.Thread(target=handle_client, args=(network,))
	thread.start()
