# Visualizer class

import pygame
import math
pygame.font.init()


class Visualizer:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 255
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	TEAL = 118, 171, 174
	BACKGROUND_COLOR = 49, 54, 63

	FONT = pygame.font.Font('assets/font.ttf', 25)
	HEADER_FONT = pygame.font.Font('assets/font.ttf', 40)

	SIDE_PAD = 150
	TOP_PAD = 275

	def __init__(self, width, height, array):
		self.width = width
		self.height = height

		self.window = pygame.display.set_mode((width, height + 25))
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
	# Create window
	displayInformation.window.fill(displayInformation.BACKGROUND_COLOR) 

	# Display menu
	title = displayInformation.HEADER_FONT.render(f"{algo_name}", 1, displayInformation.TEAL)
	displayInformation.window.blit(title, (displayInformation.width/2 - title.get_width()/2 , 15))
	isSorting = displayInformation.FONT.render("1 - Insertion Sort | 2 - Bubble Sort | 3 - Selection Sort | 4 - Shell Sort ", 1, displayInformation.TEAL)
	displayInformation.window.blit(isSorting, (displayInformation.width/2 - isSorting.get_width()/2 , 95))
	controls = displayInformation.FONT.render("Spacebar - Sort Array | R - Reset Array", 1, displayInformation.TEAL)
	displayInformation.window.blit(controls, (displayInformation.width/2 - controls.get_width()/2 , 125))
	displayArray(displayInformation)
	pygame.display.update()


# This function displays the array from a given state
def displayArray(displayInformation, color_positions={}, clearBackground=False):
	array = displayInformation.array

	if clearBackground:
		clear_rect = (displayInformation.SIDE_PAD//2, displayInformation.TOP_PAD, 
			displayInformation.width - displayInformation.SIDE_PAD, displayInformation.height - displayInformation.TOP_PAD)
		pygame.draw.rect(displayInformation.window, displayInformation.BACKGROUND_COLOR, clear_rect)

	for i, val in enumerate(array):
		x = displayInformation.start_x + i * displayInformation.block_width
		y = displayInformation.height - (val - displayInformation.min_val) * displayInformation.block_height

		color = displayInformation.WHITE

		if i in color_positions:
			color = color_positions[i] 
   
		pygame.draw.rect(displayInformation.window, color, (x, y, displayInformation.block_width, displayInformation.height))
		pygame.draw.rect(displayInformation.window, displayInformation.BLACK, (x, y, displayInformation.block_width, displayInformation.height),2)
		

	if clearBackground:
		pygame.display.update()
