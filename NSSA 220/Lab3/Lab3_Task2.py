#!/usr/bin/python
#Take in file names and create arrays for each intake
filenameOriginal = input("md5sum Original: ")
filenameModified = input("md5sum Modified: ")
fileExecutable = []
fileMD5Sum1 = []
fileMD5Sum2 = []
#Read original
with open(filenameOriginal, 'r') as f:
	for line in f:
		if '[' in line:
			continue
		data = line.strip().split()
		fileExecutable.append(data[0])
		fileMD5Sum1.append(data[1])
#Read modified
with open(filenameModified, 'r') as f:
	for line in f:
		if '[' in line:
			continue
		fileMD5Sum2.append(line.strip().split()[1])
#Compare
for i in range(len(fileMD5Sum2)):
	if fileMD5Sum1[i] != fileMD5Sum2[i]:
		print("{0}: MD5 original = {1}, MD5 new = {2}".format(fileExecutable[i], fileMD5Sum1[i], fileMD5Sum2[i]))
