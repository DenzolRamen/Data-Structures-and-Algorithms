
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def twoSum(array, target):
	lookBack = {}
	for i in range(0, len(array)):
		if array[i] in lookBack:
			return [lookBack[array[i]], i]
		else:
			lookBack[target-array[i]] = i

#answer = twoSum([2, 7, 11, 15], 9)
#answer = twoSum([1,2,3,9], 8)
#answer = twoSum([1,2,4,4], 8)
answer = twoSum([1,4,2,4], 8)
print(answer)

