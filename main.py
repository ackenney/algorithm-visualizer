import random
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


if __name__== "__main__": 
    sortedArray = [1,2,3,4,5,6,7,8,9,10]
    unsortedArray = [9, 2, 3, 5, 7, 10, 8, 4, 6, 1]
    #random.shuffle(sortedArray)
    
    print(unsortedArray)    
    print(selectionSort(unsortedArray))