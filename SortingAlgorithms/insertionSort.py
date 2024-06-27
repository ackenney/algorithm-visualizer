# insertion sort function
def insertionSort(unsortedArray):
    indexLength = range(1,len(unsortedArray))
    
    for i in indexLength:
        sortingIndex = unsortedArray[i]
        
        while (unsortedArray[i-1] > sortingIndex and i>0):
            unsortedArray[i], unsortedArray[i-1] = unsortedArray[i-1], unsortedArray[i]
            i = i - 1
    return unsortedArray