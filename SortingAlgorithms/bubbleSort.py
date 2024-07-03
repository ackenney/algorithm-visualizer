# Bubble sort function

from visualizer import displayArray


def bubbleSort(displayInformation):
    
    # Start with unsorted array
	array = displayInformation.array 

	for i in range(len(array) - 1):
		for j in range(len(array) - 1 - i):

			if (array[j] > array[j + 1]):
				# Swap positions if element found is greater
				array[j], array[j + 1] = array[j + 1], array[j]
    
				# Display array
				displayArray(displayInformation, {j: displayInformation.GREEN, j + 1: displayInformation.RED}, True)
				yield True
	
 	# Return sorted array
	return array 


