import random
import pygame
import pygame
import random
from visualizer import Visualizer, displayWindow
from SortingAlgorithms.bubbleSort import bubbleSort
from SortingAlgorithms.insertionSort import insertionSort

#FIXME
def mergeSort():
    pass


#FIXME
def heapSort():
    pass



if __name__== "__main__": 
    
    sortedArray = [1,2,3,4,5,6,7,8,9,10]
    unsortedArray = [9, 2, 3, 5, 7, 10, 8, 4, 6, 1]
    #random.shuffle(sortedArray)
    
    #print(unsortedArray)    
    #print(selectionSort(unsortedArray))
    
    run = True
    clock = pygame.time.Clock()
    displayArray = Visualizer(800,600,unsortedArray)
    sorting = False
    currentAlgorithm = bubbleSort
    algorithmName = "Bubble Sort"
    currentAlgorithmNext = None
    
    
    while run:
        clock.tick(60)
        displayWindow(displayArray, algorithmName)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            bubbleSort(displayArray)
            if event.type == pygame.K_SPACE and sorting == False:
                sorting = True
                
    pygame.quit()