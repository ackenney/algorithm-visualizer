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