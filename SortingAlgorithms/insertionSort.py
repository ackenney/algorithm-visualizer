# Implementation of Insertion Sort

from visualizer import displayArray

def insertionSort(displayInformation):
	array = displayInformation.array # Start with unsorted array
	arrayLength = len(array) # Get the length of the array
    
    # If length is 0 or 1, it is already sorted
	if arrayLength <= 1: 
		return  
 
	for i in range(1, arrayLength):
		key = array[i] 
		j = i-1
		while j >= 0 and key < array[j]:  # While greater than the key shift one position ahead
			array[j+1] = array[j]  # Shift values to the right
			j -= 1
			array[j+1] = key 
			
   			# Display array at current state
			displayArray(displayInformation, {i : displayInformation.GREEN, j: displayInformation.RED},True)
			yield True
	return array # Return sorted array