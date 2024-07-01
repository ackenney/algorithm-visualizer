# selction sort function

from visualizer import displayArray


def selectionSort(displayInformation):
    unsortedArray = displayInformation.array
    indexLength = range(0,len(unsortedArray)-1)
    
    for i in indexLength:
        minimumValue = i
        
        for j in range(i+1,len(unsortedArray)):
            if unsortedArray[j] < unsortedArray[minimumValue]:
                minimumValue = j
                displayArray(displayInformation, {j: displayInformation.RED, i: displayInformation.GREEN}, True)
                yield 
        if minimumValue != i:
            unsortedArray[minimumValue], unsortedArray[i] = unsortedArray[i], unsortedArray[minimumValue]
            #displayArray(displayInformation, {i: displayInformation.GREEN, j: displayInformation.RED}, True)
            #yield True
    return unsortedArray