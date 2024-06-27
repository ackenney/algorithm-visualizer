import random
import pygame
from SortingAlgorithms import selectionSort
from SortingAlgorithms import bubbleSort
from SortingAlgorithms import quickSort
from SortingAlgorithms import insertionSort
    
#FIXME
def mergeSort():
    pass


#FIXME
def heapSort():
    pass


pygame.init()

class DrawInfo:
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    
    SIDE_PAD = 100
    TOP_PAD = 150
    
    
     
    def __init__(self,width,height,list):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(list)

    def set_list(self,list):
        self.list = list
        self.max_val = max(list)
        self.min_val = min(list)
        self.block_width = round((self.width - self.SIDE_PAD) / len(list))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2



def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    draw_list(draw_info)
    pygame.display.update()
    
def draw_list(draw_info):
    list = draw_info.list
    
    for i, value in enumerate(list):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (value - draw_info.min_val) * draw_info.block_height
        color = draw_info.GREY
        pygame.draw.rect(draw_info.window, color,(x,y,draw_info.block_width, draw_info.height))

if __name__== "__main__": 
    
    sortedArray = [1,2,3,4,5,6,7,8,9,10]
    unsortedArray = [9, 2, 3, 5, 7, 10, 8, 4, 6, 1]
    #random.shuffle(sortedArray)
    
    print(unsortedArray)    
    #print(selectionSort(unsortedArray))
    
    run = True
    clock = pygame.time.Clock()
    draw_info = DrawInfo(800,600,unsortedArray)
    
    
    while run:
        clock.tick(60)
        draw(draw_info)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()