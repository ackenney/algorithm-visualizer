from visualizer import displayArray


def insertionSort(displayInformation):
    
	array = displayInformation.array

	for i in range(1, len(array)):
		current = array[i]

		while True:
			isSorting = i > 0 and array[i - 1] > current
			
			if not isSorting:
				break

			array[i] = array[i - 1]
			i = i - 1
			array[i] = current
			displayArray(displayInformation, {i - 1: displayInformation.GREEN, i: displayInformation.RED},True)
			yield True

	return array