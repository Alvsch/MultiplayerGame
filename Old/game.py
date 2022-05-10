import pygame.draw


class Player:
	width = height = 50

	def __init__(self, name, x=0, y=0, color=(0,0,255)):
		self.name = name
		self.x = x
		self.y = y
		self.color = color
		self.velocity = 10

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

	def move(self, move):
		if move == "w":
			self.y -= self.velocity
		elif move == "a":
			self.x -= self.velocity
		elif move == "s":
			self.y += self.velocity
		elif move == "d":
			self.x += self.velocity


class Game:
	def __init__(self):
		self.players = []

	def addPlayer(self, p: Player):
		self.players.append(p)

	def updatePlayer(self, p: Player):
		for i, v in enumerate(self.players):
			if v.name == p.name:
				self.players[i] = p
				break

	def draw_players(self, screen):
		for i in self.players:
			i.draw(screen)