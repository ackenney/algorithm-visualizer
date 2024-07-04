import random
import pygame
import pygame 
import random
from visualizer import Visualizer, displayWindow
from SortingAlgorithms.bubbleSort import bubbleSort
from SortingAlgorithms.insertionSort import insertionSort
from SortingAlgorithms.selectionSort import selectionSort
from SortingAlgorithms.shellSort import shellSort


# The createUnsortedArray function generates an unsorted array of sequential numbers from 1 to arrayLength 
def createUnsortedArray(arrayLength):
            
	unsortedArray = [i for i in range(1,arrayLength+1)]
	random.shuffle(unsortedArray)
	return unsortedArray


if __name__== "__main__": 
    
	running = True
	clock = pygame.time.Clock()
	arrayLength = 80
	fps = 60
	
	array = createUnsortedArray(arrayLength)
	displayArray = Visualizer(1500, 1000, array)
	isSorting = False
 
 	# Change window icon
	icon = pygame.image.load('assets/logo.png') 
	pygame.display.set_icon(icon) 
	
	# Algorithm generate start
	currentAlgorithm = bubbleSort #bubble sort as default
	algorithmName = "Select Algorithm"
	currentAlgorithmNext = None

	while running:
		clock.tick(fps)
		if isSorting: # Algorithm generator
			try:
				next(currentAlgorithmNext)
			except StopIteration:
				isSorting = False
		else:
			displayWindow(displayArray, algorithmName) # Show algorithm

		for event in pygame.event.get():
			# Choice select loop
			if event.type == pygame.QUIT:
				running = False
			if event.type != pygame.KEYDOWN:
				continue
			if event.key == pygame.K_r:
				array = createUnsortedArray(arrayLength)
				displayArray.set_list(array)
				isSorting = False
			elif event.key == pygame.K_SPACE and isSorting == False:
				isSorting = True
				currentAlgorithmNext = currentAlgorithm(displayArray)
		
			#Algorithm selection process
			elif event.key == pygame.K_1 and not isSorting:
				currentAlgorithm = insertionSort
				algorithmName = "Insertion Sort"
			elif event.key == pygame.K_2 and not isSorting:
				currentAlgorithm = bubbleSort
				algorithmName = "Bubble Sort"
			elif event.key == pygame.K_3 and not isSorting:
				currentAlgorithm = selectionSort
				algorithmName = "Selection Sort"
			elif event.key == pygame.K_4 and not isSorting:
				currentAlgorithm = shellSort
				algorithmName = "Shell Sort"
			
	pygame.quit()
