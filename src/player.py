# Player behavior

import pygame

import game_object
import ids

class Player(game_object.GameObject):
	def __init__(self):
		super().__init__()

		self.x_speed = 0
		self.y_speed = 0

	def process_event(self, event):
		if event.type == pygame.KEYDOWN:
##              Figure out if it was an arrow key. If so, adjust speed
			if event.key == pygame.K_LEFT:
				self.x_speed = -3
			elif event.key == pygame.K_RIGHT:
				self.x_speed = 3
			elif event.key == pygame.K_UP:
				self.y_speed = -3
			elif event.key == pygame.K_DOWN:
				self.y_speed = 3
		
##          User released a key
		elif event.type == pygame.KEYUP:
##              If it is an arrow key, reset vector back to zero
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				self.x_speed = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				self.y_speed = 0

	def update(self):
		self.pos[0] += self.x_speed
		self.pos[1] += self.y_speed

	def draw(self, screen):
		x, y = self.pos

		# Head
		pygame.draw.ellipse(screen, ids.BLACK, [1 + x, y, 10, 10], 0)
	
		# Legs
		pygame.draw.line(screen, ids.BLACK, [5 + x, 17 + y], [10 + x, 27 + y], 2)
		pygame.draw.line(screen, ids.BLACK, [5 + x, 17 + y], [x, 27 + y], 2)
	
		# Body
		pygame.draw.line(screen, ids.RED, [5 + x, 17 + y], [5 + x, 7 + y], 2)
	
		# Arms
		pygame.draw.line(screen, ids.RED, [5 + x, 7 + y], [9 + x, 17 + y], 2)
		pygame.draw.line(screen, ids.RED, [5 + x, 7 + y], [1 + x, 17 + y], 2)

