# quick sort function

from visualizer import displayArray

def quickSort(displayInformation):
    unsortedArray = displayInformation.array
    
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
            
    displayArray(displayInformation, {newArray: displayInformation.GREEN, newArray + 1: displayInformation.RED}, True)
    newArray = quickSort(isLower) + [pivot] + quickSort(isGreater)

    return newArray