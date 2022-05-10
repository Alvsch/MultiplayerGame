import socket
from network import Network
import pygame


IP = input("IPV4: ")
PORT = int(input("PORT: "))
ADDR = (IP, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



pygame.init()

FPS = 10
WIDTH = 600
HEIGHT = 400

WALK_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GAME")

clock = pygame.time.Clock()

n = Network(client, IP)
player = n.listen()
while True:
	clock.tick(FPS)

	game = n.listen()
	screen.fill(WHITE)
	game.draw_players(screen)
	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	keys = pygame.key.get_pressed()

	if keys[pygame.K_w]:
		player.move("w")

	if keys[pygame.K_a]:
		player.move("a")

	if keys[pygame.K_s]:
		player.move("s")

	if keys[pygame.K_d]:
		player.move("d")

	n.send(player)