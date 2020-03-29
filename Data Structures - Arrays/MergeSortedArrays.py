# mergeSortedArrays([0,3,4,31], [3,4,6,30])
# mergeSortedArrays([1,3,4,6,20], [2,3,4,5,6,9,11,76])


# Brute Force solution
def mergeSortedArrays(array1, array2):
	array = array1 + array2

	for item in array:
		for i in range(0, len(array)-1):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]

	return array


# Solution 1
def mergeSortedArrays1(array1, array2):
	array1Counter = 0
	array2Counter = 0
	array = []

	while (array1Counter < len(array1)) or (array2Counter < len(array2)):
		try:
			if array1[array1Counter] < array2[array2Counter]:
				array.append(array1[array1Counter])
				lastItem = array2[array2Counter]
				array1Counter += 1
			else:
				array.append(array2[array2Counter])
				lastItem = array1[array1Counter]
				array2Counter += 1
		except:
			array.append(lastItem)
			break

	return array

# Solution 2
def mergeSortedArrays2(array1, array2):
	array1Counter = 0
	array2Counter = 0
	array = []

	while (array1Counter < len(array1)) and (array2Counter < len(array2)):
		if array1[array1Counter] < array2[array2Counter]:
			array.append(array1[array1Counter])
			array1Counter += 1
		else:
			array.append(array2[array2Counter])
			array2Counter += 1
	#print(array1[array1Counter:]) #Possible Last Item
	#print(array2[array2Counter:]) #Possible  Last Item
	return array + array1[array1Counter:] + array2[array2Counter:]

# Test
print('Brute Force Solution')
answer1 = mergeSortedArrays([0,3,4,31], [3,4,6,30])
answer2 = mergeSortedArrays([1,3,4,6,20], [2,3,4,5,6,9,11,76])
print(answer1)
print(answer2)

print('\nSolution 1')
answer1 = mergeSortedArrays1([0,3,4,31], [3,4,6,30])
answer2 = mergeSortedArrays1([1,3,4,6,20], [2,3,4,5,6,9,11,76])
print(answer1)
print(answer2)

print('\nSolution 2')
answer1 = mergeSortedArrays2([0,3,4,31], [3,4,6,30])
answer2 = mergeSortedArrays2([1,3,4,6,20], [2,3,4,5,6,9,11,76])
print(answer1)
print(answer2)