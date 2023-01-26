#!/usr/bin/python
#Luke Chrampanis

import matplotlib.pyplot as plt
import numpy as np

def process_level_read_data(filename, list, cpu, mem):
	file = open(filename, "r")
	lines = file.readlines()
	for x in lines:
		list.append(x.strip().split(","))
	file.close()
	for y in list:
		cpu.append(float(y[1]))
		mem.append(float(y[2]))

def process_level_plot(x, y1, y2, y3, y4, y5, y6, y_label):
	plt.plot(x, y1, color = 'blue', label = 'APM1')
	plt.plot(x, y2, color = 'black', label = 'APM2')
	plt.plot(x, y3, color = 'red', label = 'APM3')
	plt.plot(x, y4, color = 'green', label = 'APM4')
	plt.plot(x, y5, color = 'yellow', label = 'APM5')
	plt.plot(x, y6, color = 'cyan', label = 'APM6')
	plt.xlim(xmax = 900, xmin = 0)
	plt.ylabel(y_label)
	plt.xlabel('Time(seconds)')
	plt.legend(loc = 'upper right')

	if y_label == "CPU(%)":
		plt.ylim(ymax = 70, ymin = -1)
		plt.title('CPU Utilization over Time(sec)')
		plt.savefig('cpu.png')
		plt.close()
	elif y_label == "MEM(%)":
		plt.ylim(ymax = 10, ymin = -1)
		plt.title('Memory Utilization over Time(sec)')
		plt.savefig('memory.png')
		plt.close()
	plt.show()

def process_level_metrics():
	apm_time = []
	apm1 = []
	apm1_cpu = []
	apm1_mem = []
	process_level_read_data("APM1_metrics.csv", apm1, apm1_cpu, apm1_mem)
	for x in apm1:
		apm_time.append(int(x[0]))

	apm2 = []
	apm2_cpu = []
	apm2_mem = []
	process_level_read_data("APM2_metrics.csv", apm2, apm2_cpu, apm2_mem)

	apm3 = []
	apm3_cpu = []
	apm3_mem = []
	process_level_read_data("APM3_metrics.csv", apm3, apm3_cpu, apm3_mem)

	apm4 = []
	apm4_cpu = []
	apm4_mem = []
	process_level_read_data("APM4_metrics.csv", apm4, apm4_cpu, apm4_mem)

	apm5 = []
	apm5_cpu = []
	apm5_mem = []
	process_level_read_data("APM5_metrics.csv", apm5, apm5_cpu, apm5_mem)

	apm6 = []
	apm6_cpu = []
	apm6_mem = []
	process_level_read_data("APM6_metrics.csv", apm6, apm6_cpu, apm6_mem)

	process_level_plot(apm_time, apm1_cpu, apm2_cpu, apm3_cpu, apm4_cpu, apm5_cpu, apm6_cpu, "CPU(%)")
	process_level_plot(apm_time, apm1_mem, apm2_mem, apm3_mem, apm4_mem, apm5_mem, apm6_mem, "MEM(%)")

def system_level_read_data(filename, s, r, t, w, c):
	list = []
	file = open(filename, "r")
	lines = file.readlines()
	for x in lines:
		list.append(x.strip().split(","))
	file.close()
	for y in list:
		s.append(int(y[0]))
		r.append(int(y[1]))
		t.append(int(y[2]))
		w.append(float(y[3]))
		c.append(int(y[4]))

def system_level_plot_disk(x, y, y_label, l):
	plt.plot(x, y, color = 'purple', label = l)
	plt.ylabel(y_label)
	plt.xlabel("Time(seconds)")
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc='upper right')

	if y_label == "Disk Writes(kB/s)":
		plt.title('Hard Disk Access Rates over Time(sec)')
		plt.ylim(ymax = 13000, ymin = 7000)
		plt.savefig('disk_access.png')
		plt.close()
	elif y_label == "Disk Capacity(MB)":
		plt.title('Hard Disk Utilization over Time(sec)')
		plt.ylim(ymax = 50000, ymin = 20000)
		plt.savefig('disk_util.png')
		plt.close()

def system_level_plot_data(x, y1, y2, y_label):
	plt.plot(x, y1, color = 'pink', label = 'RX Data Rate')
	plt.plot(x, y2, color = 'cyan', label = 'TX Data Rate')
	plt.ylabel(y_label)
	plt.xlabel('Time(seconds)')
	plt.ylim(ymax = 100, ymin = 0)
	plt.xlim(xmax = 900, xmin = 0)
	plt.legend(loc = 'upper right')
	plt.title("Network Bandwidth Utilization over Time(sec)")
	plt.savefig('bandwidth.png')
	plt.close()

def system_level_metrics():
	time = []
	rx = []
	tx = []
	writes = []
	capacity = []
	system_level_read_data("system_metrics.csv", time, rx, tx, writes, capacity)

	system_level_plot_data(time, rx, tx, "Data Rate(kB/s)")
	system_level_plot_disk(time, writes, "Disk Writes(kB/s)", "Disk Writes")
	system_level_plot_disk(time, capacity, "Disk Capacity(MB)", "Disk Capacity")

def main():
	print("running\n")
	process_level_metrics()
	system_level_metrics()

main()
