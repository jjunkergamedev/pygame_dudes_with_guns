
import pygame
from pygame.locals import *

FRAMES_PER_SECOND = 30

def run():
	print("running...")
	screen = pygame.display.set_mode((1024, 768))
	clock = pygame.time.Clock()
	shouldQuit = False

	# game loop
	while True:
		deltaTime = clock.tick(FRAMES_PER_SECOND)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				shouldQuit = True

			if not hasattr(event, 'key'):
				continue
			if event.key == K_ESCAPE:
				shouldQuit = True

		if shouldQuit:
			break

		screen.fill((0, 0, 0))
		pygame.display.flip()

if __name__ == "__main__":
	run()
