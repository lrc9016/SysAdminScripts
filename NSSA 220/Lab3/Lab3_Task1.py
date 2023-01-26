#!/usr/bin/python

#Intake filepath to read and empty array to return data to
def read_data(filepath, list):
	#Initialize Arrays to return with data
	sepalLength = []
	sepalWidth = []
	petalLength = []
	petalWidth = []
	irisType = []
	#Append Data to Arrays
	with open(filepath, 'r') as f:
		for line in f:
			if '@DATA' in line:
				for line in f:
					data = line.strip().split(",")
					sepalLength.append(float(data[0]))
					sepalWidth.append(float(data[1]))
					petalLength.append(float(data[2]))
					petalWidth.append(float(data[3]))
					irisType.append(data[4])
	#Append Arrays of Data to Array to return
	list.append(sepalLength)
	list.append(sepalWidth)
	list.append(petalLength)
	list.append(petalWidth)
	list.append(irisType)
	#Close file and return
	f.close()
	return list

#Intake array of irisType and empty array to return data to
def count_iris_type(irisTypes, list):
	#Initialize counters
	irisSe = 0
	irisVe = 0
	irisVi = 0
	#Loop through list to increment counters
	for i in irisTypes:
		if i == "Iris-setosa":
			irisSe += 1
		if i == "Iris-versicolor":
			irisVe += 1
		if i == "Iris-virginica":
			irisVi += 1
	#Append counters final value to Array to return
	list.append(irisSe)
	list.append(irisVe)
	list.append(irisVi)
	#Return
	return(list)

#Intake array of read data, index of array to read, and empty array to return data to
def process_numeric_field(dataList, index, list):
	#Initialize blank values
	minimum = 0
	maximum = 0
	average = 0
	#Find min
	minimum = min(dataList[index])
	#Find max
	maximum = max(dataList[index])
	#Find avg
	average = sum(dataList[index]) / len(dataList[index])
	avgStr = str(round(average, 2))
	#Append values to Array to return
	list.append(minimum)
	list.append(maximum)
	list.append(avgStr)
	#Return
	return(list)

#Read a filename
filename = input("Filename: ")
#Initialize empty list
emptyList = []
#Read data and store in variable
data = read_data(filename, emptyList)
#Initialize list of names of the first four fields
fields = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
#Loop to find values of first four fields
for i in range(4):
	emptyList = []
	values = process_numeric_field(data, i, emptyList)
	print("{0}: min={1}, max={2}, average={3}".format(str(fields[i]), str(values[0]), str(values[1]), str(values[2])))
#Count Iris Types and store in variable
emptyList = []
iris = count_iris_type(data[-1], emptyList)
print("Iris Types: Iris Setosa={0}, Iris Versicolor={1}, Iris Virginica={2}".format(str(iris[0]), str(iris[1]), str(iris[2])))
