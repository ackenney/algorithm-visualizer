import random

    
#FIXME
def mergeSort():
    pass


# quick sort functions
def quickSort(unsortedArray):
    
    
    isGreater =[]
    isLower = []
    
    length = len(unsortedArray)
    
    if length <= 1:
        return unsortedArray;
    else:
        pivot = unsortedArray.pop()
    
    for index in unsortedArray:
        if index > pivot:
             isGreater.append(index)
        else:
            isLower.append(index)
            
    newArray = quickSort(isLower) + [pivot] + quickSort(isGreater)

    return newArray




#FIXME
def heapSort():
    pass


#FIXME
def insertionSort():
    pass


#FIXME
def bubbleSort():
    pass



if __name__== "__main__": 
    sortedArray = [1,2,3,4,5,6,7,8,9,10]
    unsortedArray = [9, 2, 3, 5, 7, 10, 8, 4, 6, 1]
    #random.shuffle(sortedArray)
    
    print(unsortedArray)    
    print(quickSort(unsortedArray))