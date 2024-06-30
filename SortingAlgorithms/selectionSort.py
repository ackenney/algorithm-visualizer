# selction sort function

from visualizer import displayArray


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