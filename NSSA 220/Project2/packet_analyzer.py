from filter_packets import *
from packet_parser import *
from compute_metrics import *


def outputCSV(metrics):
    outputFile = open("project2Output.csv", "+w")
    i = 1
    for r in metrics:
        outputFile.write("Node " + str(i))
        i += 1
        outputFile.write("\n")
        outputFile.write("\n")
        outputFile.write("Echo Requests Sent,Echo Requests Received,Echo Replies Sent,Echo Replies Received")
        outputFile.write("\n")
        outputFile.write(str(r[0]) + "," + str(r[1]) + "," + str(r[2]) + "," + str(r[3]))
        outputFile.write("\n")
        outputFile.write("Echo Request Bytes Sent (bytes),Echo Request Data Sent (bytes)")
        outputFile.write("\n")
        outputFile.write(str(r[4]) + "," + str(r[6]))
        outputFile.write("\n")
        outputFile.write("Echo Request Bytes Received (bytes),Echo Request Data Received (bytes)")
        outputFile.write("\n")
        outputFile.write(str(r[5]) + "," + str(r[7]))
        outputFile.write("\n")
        outputFile.write("\n")
        outputFile.write("Average RTT (milliseconds)," + str(r[8]))
        outputFile.write("\n")
        outputFile.write("Echo Request Throughput (kB/sec)," + str(r[9]))
        outputFile.write("\n")
        outputFile.write("Echo Request Goodput (kB/sec)," + str(r[10]))
        outputFile.write("\n")
        outputFile.write("Average Reply Delay (microseconds)," + str(r[11]))
        outputFile.write("\n")
        outputFile.write("Average Echo Request Hop Count," + str(r[12]))
        outputFile.write("\n")
        outputFile.write("\n")


filter()
node1Data, node2Data, node3Data, node4Data = parse()
node1Metrics, node2Metrics, node3Metrics, node4Metrics = compute(node1Data, node2Data, node3Data, node4Data)
outputCSV([node1Metrics, node2Metrics, node3Metrics, node4Metrics])
