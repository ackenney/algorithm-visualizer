import pygame
import math
pygame.font.init()


class Visualizer:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	BACKGROUND_COLOR = WHITE

	FONT = pygame.font.SysFont('ariel', 30)
	LARGE_FONT = pygame.font.SysFont('ariel', 40)

	SIDE_PAD = 100
	TOP_PAD = 150

	def __init__(self, width, height, array):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Sorting Algorithm Visualization")
		self.set_list(array)

	def set_list(self, array):
		self.array = array
		self.min_val = min(array)
		self.max_val = max(array)

		self.block_width = round((self.width - self.SIDE_PAD) / len(array))
		self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
		self.start_x = self.SIDE_PAD // 2

def displayWindow(displayInformation, algo_name):
	displayInformation.window.fill(displayInformation.BACKGROUND_COLOR)


	font = pygame.font.SysFont('Georgia',40,bold=True)
	surf = font.render('Quit', True, 'black')
	button = pygame.Rect(200,200,110,60)

	title = displayInformation.LARGE_FONT.render(f"{algo_name}", 1, displayInformation.BLACK)
	displayInformation.window.blit(title, (displayInformation.width/2 - title.get_width()/2 , 5))

	controls = displayInformation.FONT.render("R - Reset | SPACE - Start Sorting", 1, displayInformation.BLACK)
	displayInformation.window.blit(controls, (displayInformation.width/2 - controls.get_width()/2 , 45))

	isSorting = displayInformation.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, displayInformation.BLACK)
	displayInformation.window.blit(isSorting, (displayInformation.width/2 - isSorting.get_width()/2 , 75))

	displayArray(displayInformation)
	pygame.display.update()


def displayArray(displayInformation, color_positions={}, clear_bg=False):
	array = displayInformation.array

	if clear_bg:
		clear_rect = (displayInformation.SIDE_PAD//2, displayInformation.TOP_PAD, 
						displayInformation.width - displayInformation.SIDE_PAD, displayInformation.height - displayInformation.TOP_PAD)
		pygame.draw.rect(displayInformation.window, displayInformation.BACKGROUND_COLOR, clear_rect)

	for i, val in enumerate(array):
		x = displayInformation.start_x + i * displayInformation.block_width
		y = displayInformation.height - (val - displayInformation.min_val) * displayInformation.block_height

		color = displayInformation.BLACK

		if i in color_positions:
			color = color_positions[i] 

		pygame.draw.rect(displayInformation.window, color, (x, y, displayInformation.block_width, displayInformation.height))

	if clear_bg:
		pygame.display.update()
