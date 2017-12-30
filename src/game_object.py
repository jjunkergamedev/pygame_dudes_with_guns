# Base Game Object class.

class GameObject():
	def __init__(self):
		self.pos = [0, 0]

	def process_event(self, event):
		pass

	def update(self):
		pass

	def draw(self, screen):
		pass
