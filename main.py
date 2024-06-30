import random
import pygame
import pygame
import random
from visualizer import Visualizer, displayWindow
from SortingAlgorithms.bubbleSort import bubbleSort
from SortingAlgorithms.insertionSort import insertionSort


# The createUnsortedArray function generates an unsorted array of sequential numbers from 1 to arrayLength 
def createUnsortedArray(arrayLength):
            
	unsortedArray = [i for i in range(1,arrayLength)]
	random.shuffle(unsortedArray)
	return unsortedArray


if __name__== "__main__": 
	running = True
	clock = pygame.time.Clock()

	arrayLength = 50
	
	array = createUnsortedArray(arrayLength)
	displayArray = Visualizer(1500, 1000, array)
	isSorting = False
 
	icon = pygame.image.load('assets/logo.png') 
	pygame.display.set_icon(icon) # Change window icon
	

	currentAlgorithm = bubbleSort
	algorithmName = "Select Algorithm"
	currentAlgorithmNext = None

	while running:
		clock.tick(60)
		if isSorting:
			try:
				next(currentAlgorithmNext)
			except StopIteration:
				isSorting = False
		else:
			displayWindow(displayArray, algorithmName)

		for event in pygame.event.get():
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
			
			elif event.key == pygame.K_i and not isSorting:
				currentAlgorithm = insertionSort
				algorithmName = "Insertion Sort"
			elif event.key == pygame.K_b and not isSorting:
				currentAlgorithm = bubbleSort
				algorithmName = "Bubble Sort"
			elif event.key == pygame.K_q and not isSorting:
				currentAlgorithm = bubbleSort
				algorithmName = "Quick Sort"
			elif event.key == pygame.K_s and not isSorting:
				currentAlgorithm = bubbleSort
				algorithmName = "Selection Sort"
			elif event.key == pygame.K_m and not isSorting:
				currentAlgorithm = bubbleSort
				algorithmName = "Merge Sort"
    


	pygame.quit()
