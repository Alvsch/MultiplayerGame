import socket
import threading

from game import Game
from network import *

IP = socket.gethostbyname(socket.gethostname())

PORT = 5050
ADDR = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connections = 0
game = Game()

def handle_client(network: Network):
	global game, connections
	print(f"New Connection From {network.getAddress()}")

	connections += 1

	while True:
		network.send(game)


server.listen()
print(f"Started Server On IP: {IP} and PORT: {PORT}")

while True:
	conn, addr = server.accept()
	network = Network(conn, addr)

	thread = threading.Thread(target=handle_client, args=(network,))
