# no libraries are allowed

def partition(start, end, array):
	
	# Initializing pivot's index to start
	pivot_index = start
	pivot = array[pivot_index][1]
	
	while start < end:
		while start < len(array) and array[start][1] <= pivot:             # Traverse from start until you find element greater than pivot
			start += 1
			
		while array[end][1] > pivot:                                       # Traverse from end until you find element greater than pivot
			end -= 1
		
		if(start < end):                                                
			array[start], array[end] = array[end], array[start]                 # Swap if pointers dont cross each other
	
	array[end], array[pivot_index] = array[pivot_index], array[end]             # Swapping of elements in place
	
	return end
	
def quicksort(start, end, array):
	
	if (start < end):
		
		partIndex = partition(start, end, array)
		
		quicksort(start, partIndex - 1, array)
		quicksort(partIndex + 1, end, array)
		

def k_closest_points(x_array, y_array, point, k):
    """
    (list of float, list of float, tuple of two floats, int) -> (list of float), (list of float)
    
    >>> k_closest_points([1.0, 1.0, 3.0, 5.0], [0.0, 3.0, 4.0, 5.0], (0.0, 0.0), 2)
        [1.0, 1.0], [0.0, 3.0]
    """

    if(len(x_array) != len(y_array)):
        raise Exception ("Invalid input")
        return
    
    arr = []
    for i in range(len(x_array)):
        arr.append((i, ((x_array[i]**2) + (y_array[i]**2))**(0.5)))         # Calculate the Euclidean distance

    # arr.sort(key = lambda x : x[1])
    quicksort(0, len(arr) - 1, arr)                 # Sort the coordinates with respect to the Euclidean distance
    
    x_close = []
    y_close = []

    for i in arr[:k]:                           # Get the first k-elements
        x_close.append(x_array[i[0]])
        y_close.append(y_array[i[0]])

    return (x_close, y_close)

print(k_closest_points([1.0, 1.0, 3.0, 5.0], [0.0, 3.0, 4.0, 5.0], (0.0, 0.0), 2))
