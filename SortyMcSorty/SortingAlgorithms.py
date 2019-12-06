import numpy as np
#Array that was being used for testing#
array = [1, 4, 23, 76, 7, 31, 12, -19, 0.01, 123, -321, 0.5, 1023, -33]
import time


#Creating Random Array, with num amount of elements#
def rand_function(num):
	arr = []
	for i in range(num):
		random_number = int(np.random.rand()*100)
		arr.append(random_number)
	return arr

#Bubble Sort Algorithm#
def bubbleSort(data):
	i = len(data)
	while i > 0:
		j = 0
		while j < i - 1:
			if(data[j] > data[j+1]):
				t = data[j]
				data[j] = data[j+1]
				data[j + 1] = t
			j = j + 1
		i = i - 1
	return(data)

#MDoesn't actually sort in this algorithm, instead uses recursion#
def mergeSort(data):
	#Terminating Conditions#
	if(len(data) <= 1):
		return data
	if(len(data) == 2):
		if(data[0] > data[1]):
			return [data[1], data[0]]
		else:
			return data
	
	#Splits the arrays, and recurses until there are a certain amount of array with lenghts of 2, then sorts#
	half = len(data)//2
	a, b = data[:half], data[half:]
	left = mergeSort(a)
	right = mergeSort(b)
	sortedArray = Sorter(left, right)
	return sortedArray


#Sorts the arrays it takes in#
def Sorter(left, right):
	i = 0
	j = 0

	sortedArray = []

	total_length = len(left) + len(right)

	for i in range(total_length):

		if len(left) == 0:
			sortedArray += right
			return sortedArray

		if len(right) == 0:
			sortedArray += left
			return sortedArray

		left_val = left[0]
		right_val = right[0]

		if (left_val < right_val):
			sortedArray.append(left_val)
			left = left[1:]
		else:
			sortedArray.append(right_val)
			right = right[1:]


#Creating the Array of 100,000 elements#
rand_array = rand_function(100000)
#Timing the 2 sorting algorithms
start_merge = time.time()
merged = mergeSort(rand_array)
end_merge = time.time()
print("merge time:", end_merge - start_merge)

start_bubble = time.time()
bubble = bubbleSort(rand_array)
end_bubble = time.time()
print("bubble time:", end_bubble - start_bubble)

##Merge sort took 21 seconds to sort the array of 100,000. Bubble sort took 1,537 seconds to sort it##

