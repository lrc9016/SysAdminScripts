def parse() :
	node1Data = parse_nodeFile("Node1_filtered.txt")
	node2Data = parse_nodeFile("Node2_filtered.txt")
	node3Data = parse_nodeFile("Node3_filtered.txt")
	node4Data = parse_nodeFile("Node4_filtered.txt")
	return node1Data,node2Data,node3Data,node4Data

def parse_nodeFile(fn_filename):
	f = open(fn_filename)
	records = f.readlines()
	nodeInfo = []
	readLine = False
	for r in records:
		if readLine:
			lineInfo = r.split()
			pingRecord = []
			pingRecord.append(float(lineInfo[1]))
			pingRecord.append(lineInfo[2])
			pingRecord.append(lineInfo[3])
			pingRecord.append(float(lineInfo[5]))
			pingRecord.append(float(lineInfo[5]) - 42)
			pingRecord.append(lineInfo[8])
			nodeInfo.append(pingRecord)
			readLine=False
		elif "No." in r:
			readLine = True
	return nodeInfo
