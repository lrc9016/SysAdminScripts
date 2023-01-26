from filter_packets import *
from packet_parser import *

def compute(node1Data, node2Data,node3Data, node4Data):
	node1Metrics = compute_metrics("192.168.100.1", node1Data)
	node2Metrics = compute_metrics("192.168.100.2", node2Data)
	node3Metrics = compute_metrics("192.168.200.1", node3Data)
	node4Metrics = compute_metrics("192.168.200.2", node4Data)

	return node1Metrics,node2Metrics,node3Metrics,node4Metrics





def compute_metrics(ip, list):
	echo_requests_sent = 0
	echo_requests_recv = 0
	echo_replies_sent = 0
	echo_replies_recv = 0
	echo_requests_bytes_sent = 0
	echo_requests_bytes_recv = 0
	echo_requests_data_sent = 0
	echo_requests_data_recv = 0

	total_time1 = 0
	total_time2 = 0
	counter1 = 0
	counter2 = 0

	average_rtt = 0
	average_reply_delay = 0

	echo_throughput = 0
	echo_goodput = 0

	hop_count = 0  # RELATED TO HOPS ------------------------------------------------------------------------------------------------------------------------------------------

	for data in list:
		if data[5] == "reply":
			if data[1] == ip:
				echo_replies_sent += 1
			elif data[2] == ip:
				echo_replies_recv += 1
		if data[5] == "request":
			if data[1] == ip:
				echo_requests_sent += 1
				echo_requests_bytes_sent += int(data[3])
				echo_requests_data_sent += int(data[4])
			if data[2] == ip:
				echo_requests_recv += 1
				echo_requests_bytes_recv += int(data[3])
				echo_requests_data_recv += int(data[4])

	# Average Round Trip Time, Goodput, Throughput
	for i in range(0, len(list)):
		if list[i][5] == "request":
			if list[i][1] == ip:
				counter1 += 1
				total_time1 += (float(list[i + 1][0]) - float(list[i][0]))

	# Average Reply Delay
	for i in range(0, len(list)):
		if list[i][5] == "request":
			if list[i][2] == ip:
				counter2 += 1
				total_time2 += (float(list[i + 1][0]) - float(list[i][0]))

	# Hop metrics processing ---------------------------------------------
	for data in list:
		if data[5] == "request" and data[1] == ip:
			hop_count += compare_network(data[1], data[2])


	request_throughput = (echo_requests_bytes_sent / total_time1) / 1000  # Divide by 1000 to make ms to sec
	request_goodput = (echo_requests_data_sent / total_time1) / 1000
	average_rtt = (total_time1 / counter1) * 1000
	average_reply_delay = (total_time2 / counter2) * 1000000
	average_hop = float(hop_count) / float(echo_requests_sent)  # -------------------------------------------------------------------------------------------------------------

	return [echo_requests_sent, echo_requests_recv, echo_replies_sent, echo_replies_recv, round(echo_requests_bytes_sent, 2), round(
		echo_requests_bytes_recv, 2), round(echo_requests_data_sent, 2), round(echo_requests_data_recv, 2), round(
		average_rtt, 2), round(request_throughput, 1), round(request_goodput, 1), round(average_reply_delay, 2), round(
		average_hop, 2)]


def compare_network(a, b):
	aPart = a.split(".")
	bPart = b.split(".")
	for i in [0,1,2]:
		if aPart[i] != bPart[i]:
			return 3
	return 1
