# bubble sort function
from visualizer import displayArray


def bubbleSort(displayInformation):
	array = displayInformation.array

	for i in range(len(array) - 1):
		for j in range(len(array) - 1 - i):
			num1 = array[j]
			num2 = array[j + 1]
   
			if (num1 > num2):
				array[j], array[j + 1] = array[j + 1], array[j]
				displayArray(displayInformation, {j: displayInformation.GREEN, j + 1: displayInformation.RED}, True)
				yield True

	return array


