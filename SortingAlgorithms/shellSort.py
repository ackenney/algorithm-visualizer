# Implementation of Shell Sort function


from visualizer import displayArray

def shellSort(displayInformation):
    array = displayInformation.array # Start with unsorted array
    arrayLength = len(array) # Get length
    gap = arrayLength // 2 # Get starting array gap


    # while there is still a gap / array is unsorted
    while gap > 0:
        for i in range(gap, arrayLength):
            temp = array[i]

            # move sorted values
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            array[j] = temp
            
   			# Display array at current state
            displayArray(displayInformation, {i: displayInformation.GREEN, j: displayInformation.RED}, True)
            yield 
        gap //= 2 # Reduce gap
    return array # Return sorted array