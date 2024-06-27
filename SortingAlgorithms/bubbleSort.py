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
