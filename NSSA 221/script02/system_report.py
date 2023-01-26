#!/usr/bin/env python3
#Luke Chrampanis   |   9/30/22
#Script 02   |   System Administration

#Import necessary libraries
import os;
import sys;
from datetime import date;
import socket;
import subprocess;

#Create class for colors that will be reused throughout report
class colors:
	HEADER = '\033[95m';
	BLUE = '\033[94m';
	GREEN = '\033[92m';
	END = '\033[0m';

#Clear terminal
os.system("clear");

#Print a header for the report
def printHeader():
	print(colors.HEADER + "SYSTEM REPORT - " + str(date.today()) + colors.END + "\n");

#Print the device information
def printDeviceInformation():
	print(colors.GREEN + "Device Information" + colors.END);
	fqdn = socket.getfqdn();
	deviceInformation = fqdn.split(".");
	print("Hostname: " + deviceInformation[0]);
	print("Domain: " + deviceInformation[1] + "." + deviceInformation[2]);
	print();

#Print the network information
def printNetworkInformation():
	print(colors.GREEN + "Network Information" + colors.END);
	temp = str(subprocess.check_output("ifconfig | grep inet", shell=True)).split(" ");
	netInfo = list(filter(None, temp));
	temp = str(subprocess.check_output("cat /etc/resolv.conf", shell=True)).split(" ");
	dnsInfo = list(filter(None, temp));
	print("IP Address: " + netInfo[2]);
	print("Gateway: " + netInfo[6].split("\\")[0]);
	print("Network Mask: " + netInfo[4]);
	print("DNS1: " + dnsInfo[5].split("\\")[0]);
	print("DNS2: " + dnsInfo[6].split("\\")[0]);
	print();

#Print the OS information
def printOsInformation():
	print(colors.GREEN + "OS Information" + colors.END);
	temp = str(subprocess.check_output("cat /etc/os-release | head -n 2", shell=True)).split("\"");
	osInfo = list(filter(None, temp));
	kernelVersion = str(subprocess.check_output("uname -r", shell=True));
	print("Operating System: " + osInfo[1]);
	print("Operating Version: " + osInfo[3]);
	print("Kernel Version: " + kernelVersion.split("\'")[1].split("\\")[0]);
	print();

#Print storage information
def printStorageInformation():
	print(colors.GREEN + "Storage Information" + colors.END);
	temp = str(subprocess.check_output("df -h --total | grep total", shell=True)).split(" ");
	storInfo = list(filter(None, temp));
	print("Hard Drive Capacity: " + storInfo[1]);
	print("Available Space: " + storInfo[3]);
	print();

#Print processor information
def printProcessorInformation():
	print(colors.GREEN + "Processor Information" + colors.END);
	temp = str(subprocess.check_output("lscpu", shell=True)).split(" ");
	procInfo = list(filter(None, temp));
	temp = str(subprocess.check_output("lscpu | grep name", shell=True)).split(" ");
	modelName = list(filter(None, temp));
	name = "";
	for i in modelName:
		if(i != "b'Model" and i != "name:"):
			name += i + " ";
	print("CPU Model: " + name.split("\\")[0]);
	print("Number of Processors: " + procInfo[8].split("\\")[0]);
	print("Number of Cores: " + procInfo[17].split("\\")[0]);
	print();

#Print memory information
def printMemoryInformation():
	print(colors.GREEN + "Memory Information" + colors.END);
	temp = str(subprocess.check_output("free -h", shell=True)).split(" ");
	memInfo = list(filter(None, temp));
	print("Total RAM: " + memInfo[7]);
	print("Available RAM: " + memInfo[12].split("\\")[0]);
	print();

#Call all print functions
printHeader();
printDeviceInformation();
printNetworkInformation();
printOsInformation();
printStorageInformation();
printProcessorInformation();
printMemoryInformation();

#Write output to log file and ensure file doesn't run keep running itself
if (len(sys.argv) != 2):
	os.system("python3 system_report.py 1 > " + str(socket.getfqdn()).split(".")[0] + "_system_report.log")
else:
	pass
