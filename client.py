import pygame

from game import *
import socket
from network import *

IP = input("IPV4: ")
PORT = int(input("PORT: "))
ADDR = (IP, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

pygame.init()
screen = Screen(600, 400)
clock = pygame.time.Clock()


net = Network(client, ADDR)
p = net.listen()

FPS = 30
while True:
	clock.tick(FPS)

	game = net.listen()
	game.draw(screen.getScreen())
	screen.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		p.move("w")
	if keys[pygame.K_a]:
		p.move("a")
	if keys[pygame.K_s]:
		p.move("s")
	if keys[pygame.K_d]:
		p.move("d")

	net.send(p)