def filter():
	filterFile(1)
	filterFile(2)
	filterFile(3)
	filterFile(4)

	



def filterFile(num):
	f = open("Node"+str(num)+".txt")
	records = f.readlines()
	newFile = open("Node"+ str(num) + "_filtered.txt", "w")
	writeLine = False
	newNode = False
	storeLine = ""
	for r in records:
		if "No." in r:
			storeLine = r
			newNode = True
		elif newNode:
			if "Echo" in r:
				newFile.write(storeLine)
				newFile.write(r)
				writeLine = True
			else:
				writeLine = False
			newNode = False
		elif writeLine:
			newFile.write(r)


filter()
