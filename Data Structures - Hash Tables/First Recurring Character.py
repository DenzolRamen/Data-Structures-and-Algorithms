array1 = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array2 = [2, 1, 1, 2, 3, 5, 1, 2, 4]
array3 = [2, 3, 4, 5]

# Naive approach: Using two for loops, but it will have a problem in some cases
def firstRecurringCharacter(array):
	for i in range(0, len(array)):
		for j in range(i+1, len(array)):
			if array[i] == array[j]:
				return array[i]
	return None
# 'None' is Python's 'undefined' of Java Script

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Testing
print(firstRecurringCharacter(array1))
print(firstRecurringCharacter(array2)) # This test scenario will have a problem in this solution
print(firstRecurringCharacter(array3))

# But there is a problem for situations like this:
# It will return 2 instead of 5
print(firstRecurringCharacter([2, 5, 5, 2, 3, 5, 1, 2, 4]))

print('\n')

# Solving the problem using hash table
def firstRecurringCharacter2(array):
	lookUp = {}
	# When looping a dictionary in Python, we are looping the dictionary's keys
	for i in array:
		if i in lookUp:
			return i
		else:
			lookUp[i] = True
	# Python automatically returns 'None' if the conditions were not satisfied

# Time Complexity: O(n)
# Space Complexity: O(n)

# Testing
print(firstRecurringCharacter2(array1))
print(firstRecurringCharacter2(array2))
print(firstRecurringCharacter2(array3))
print(firstRecurringCharacter2([2, 5, 5, 2, 3, 5, 1, 2, 4]))

# Hash Tables are usually the answer to improve time complexity
# But it will cause tradeoffs between time complexity and space complexity