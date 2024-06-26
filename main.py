import random

    
#FIXME
def mergeSort():
    pass


# quick sort function
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


# selction sort function
def selectionSort(unsortedArray):
    indexLength = range(0,len(unsortedArray)-1)
    
    for i in indexLength:
        minimumValue = i

        for j in range(i+1,len(unsortedArray)):
            if unsortedArray[j] < unsortedArray[minimumValue]:
                minimumValue = j
                
        if minimumValue != i:
            unsortedArray[minimumValue], unsortedArray[i] = unsortedArray[i], unsortedArray[minimumValue]
    return unsortedArray


# insertion sort function
def insertionSort(unsortedArray):
    indexLength = range(1,len(unsortedArray))
    
    for i in indexLength:
        sortingIndex = unsortedArray[i]
        
        while (unsortedArray[i-1] > sortingIndex and i>0):
            unsortedArray[i], unsortedArray[i-1] = unsortedArray[i-1], unsortedArray[i]
            i = i - 1
    return unsortedArray
            

# bubble sort function
def bubbleSort(unsortedArray):
    indexLength = len(unsortedArray) -1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0,indexLength):
            if (unsortedArray[i] > unsortedArray[i+1]):
                sorted = False
                #swap
                unsortedArray[i], unsortedArray[i+1] = unsortedArray[i+1], unsortedArray[i]
    return unsortedArray



if __name__== "__main__": 
    sortedArray = [1,2,3,4,5,6,7,8,9,10]
    unsortedArray = [9, 2, 3, 5, 7, 10, 8, 4, 6, 1]
    #random.shuffle(sortedArray)
    
    print(unsortedArray)    
    print(selectionSort(unsortedArray))