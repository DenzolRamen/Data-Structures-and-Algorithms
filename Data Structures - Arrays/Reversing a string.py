# Reverse string 'Hi I am Denzel'

# Solution 1
def reverse1(string):
	counter = len(string)-1
	newStr = []

	# Section for input checking.Start
	# Section for input checking.End

	while counter >= 0:
		newStr.append(string[counter])
		counter -= 1

	return ''.join(newStr)

# Solution 2
def reverse2(string):
	counter = len(string)-1
	newStr = ''

	# Section for input checking.Start
	# Section for input checking.End

	while counter >= 0:
		newStr+=string[counter]
		counter -= 1

	return newStr

# Solution 3
def reverse3(string):
	newStr = []

	# Section for input checking.Start
	# Section for input checking.End

	for i in range(len(string)-1, -1, -1):	#range(start, stop, step)
		newStr.append(string[i])
	return ''.join(newStr)

# Solution 4 - Pythonic Way 1
def reverse4(string):
	# Section for input checking.Start
	# Section for input checking.End
	return string[::-1]

# Solution 5 - Pythonic Way 2 (Lambda Function)
reverse5 = lambda string: string[::-1]

# Test
print('Solution 1')
print(reverse1('Hi I am Denzel'))

print('\nSolution 2')
print(reverse2('Hi I am Denzel'))

print('\nSolution 3')
print(reverse3('Hi I am Denzel'))

print('\nSolution 4')
print(reverse4('Hi I am Denzel'))

print('\nSolution 5')
print(reverse5('Hi I am Denzel'))
