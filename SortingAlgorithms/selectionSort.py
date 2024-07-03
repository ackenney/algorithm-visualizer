# Implementation of Selction Sort function

from visualizer import displayArray

def selectionSort(displayInformation):
    array = displayInformation.array
    indexLength = range(0,len(array)-1)
    
    for i in indexLength:
        minimumValue = i
        
        for j in range(i+1,len(array)):
            if array[j] < array[minimumValue]:
                minimumValue = j # Set new minimum value element
                
                # Display array at current state
                displayArray(displayInformation, {j: displayInformation.RED, i-1: displayInformation.GREEN}, True)
                yield 
        if minimumValue != i: # Swap elements if not minimum value
            array[minimumValue], array[i] = array[i], array[minimumValue]
    return array # Return sorted array