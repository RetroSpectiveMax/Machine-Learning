year = [2011, 2012, 2013, 2014, 2015, 2016]
income = [1256.0, 2578.76, 3222.50, 4598.12, 4981, 5890.99]


#Debugged#
def mean(data):
	total = 0
	for x in range(len(data)):
		total += data[x]
	return float(total) / len(data)

#Debugged#
def multiply(data1, data2):
	tempArray = []
	for x in range(len(data1)):
		tempArray.append(data1[x] * data2[x])
	return tempArray
#Debugged. Everything works#
def squareArray(data):
	tempArray = []
	for x in range(len(data)):
		tempArray.append(data[x] ** 2)
	return tempArray
def lineOfBestFit(data1, data2):
	
	#calculate components of LOBF#
	aveOfArray = mean(data1) * mean(data2)
	multArray = mean(multiply(data1, data2))
	squareAve = mean(data1) * mean(data1)
	aveSquared = mean(squareArray(data1))

	#print("avg of array", aveOfArray, "multarray", multArray, "square avg", squareAve, "avg squared", aveSquared)
	#Piece together equation#
	m = (aveOfArray - multArray) / (squareAve - aveSquared)
	print(m)
	return m

# def mean_test(array, expected):
# 	avg = mean(array)
# 	if (avg == expected):
# 		print("Mean Test Passed")
# 		return
# 	print("Mean Test Failed")

# def multiply_test(array1, array2, expected):
# 	mult = multiply(array1, array2)
# 	if (mult == expected):
# 		print("Mult Test Passed")
# 		return
# 	print("Mult Test Failed")

# def square_test(array, expected):
# 	square = squareArray(array)
# 	if (square == expected):
# 		print("Square Test Passed")
# 		return
# 	print("Square Test Failed")

# mean_test([1,2,3,4.0], 2.5)
# multiply_test([1,2,3], [1,2,3], [1,4,9])
# square_test([1,2,3,4.0], [1,4,9,16])

# year = [1,2,3]
# income = [1, 2.5, 4]
lineOfBestFit(year, income) 


def yIntercept(x, y):
	b = mean(y) - (lineOfBestFit(year, income) * mean(x))
	print("Y intercept is ", b)
	return b

yIntercept(year, income)

yearIn = int(input("What year would you like for me to predict: "))
def answer():
	print(yearIn)
	incomePred = lineOfBestFit(year, income) * yearIn + yIntercept(year, income)
	print(incomePred)
	return incomePred

answer()


