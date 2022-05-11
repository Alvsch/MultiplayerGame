import pygame
from network import *


class Player:
	width = height = 50

	def __init__(self, name, width, height, color=(0, 0, 255)):
		self.name = name
		self.x = 0
		self.y = 0
		self.color = color
		self.velocity = 5

	def move(self, move):
		if move == "w":
			self.y -= self.velocity
		elif move == "a":
			self.x -= self.velocity
		elif move == "s":
			self.y += self.velocity
		elif move == "d":
			self.x += self.velocity

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)


class Game:
	def __init__(self):
		self.players = []

	def addPlayer(self, p):
		self.players.append(p)

	def updatePlayer(self, p):
		for i, v in enumerate(self.players):
			if v.name == p.name:
				self.players[i] = p
				break

	def removePlayer(self, p):
		self.players.remove(p)

	def draw(self, screen, color):
		for p in self.players:
			p.draw(screen)


class Screen:
	def __init__(self, width, height, name="None"):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption(name)

	@staticmethod
	def update():
		pygame.display.update()

	def getScreen(self):
		return self.screen

	def draw_background(self):
		self.screen.fill((255, 255, 255))