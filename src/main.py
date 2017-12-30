
import pygame
from pygame.locals import *

import player
import ids

FRAMES_PER_SECOND = 30

def process_events(objects):
	should_quit = False

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			should_quit = True

		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				should_quit = True

		# TODO: make sure each object only listens for relevant events
		for obj in objects:
			obj.process_event(event)

	return should_quit

def update_behaviors(objects):
	for obj in objects:
		obj.update()

def render(screen, objects):
	screen.fill(ids.WHITE)

	for obj in objects:
		obj.draw(screen)

	pygame.display.flip()

def init_objects():
	result = [player.Player()]
	return result

def run():
	print("running...")
	screen = pygame.display.set_mode((1024, 768))
	pygame.display.set_caption("My Game")

	clock = pygame.time.Clock()

	objects = init_objects()

	done = False

	# game loop
	while not done:
		deltaTime = clock.tick(FRAMES_PER_SECOND)

		done = process_events(objects)

		update_behaviors(objects)

		render(screen, objects)

	pygame.quit()

if __name__ == "__main__":
	run()
