
#!/usr/bin/env python3
#Luke Chrampanis   |   11/3/22
#Script 04   |   System Administration

#Import necessary libraries and functions
import os;
import sys;
import re;
from datetime import date;
from collections import Counter;
from geoip import geolite2;

#Clears terminal
os.system("clear");

#Read the input file as a system argument
file = str(sys.argv[1]);
file_obj = open(file, "r");
file_data = file_obj.read();
#Split the file into lines
lines = file_data.splitlines();

#Create pattern to search for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})');
ip_addrs = [];
#For every line check if there is a failure to login and then take the ip address from that line and store it
for line in lines:
	if ("Failed" in line):
		temp = str(pattern.search(line)).split("\'");
		if (len(temp) > 1):
			ip_addrs.append(temp[1]);
#Count duplicate values and assign them to the ips in a dictionary only if there are 10 or more duplicate values
counts = dict(Counter(ip_addrs))
duplicates = {key:value for key, value in counts.items() if value >= 10}
#Create list of ips in ascending order of count
duplicates_list = sorted(duplicates, key=duplicates.get)

#========================================================================
#Output + Formatting
print("Attacker Report - " + str(date.today()))
print("\033[95m" + "COUNT\tIP ADDRESS\tCOUNTRY" + "\033[0m")
#For value in sorted list, print key and value from dictionary as well as country  of origin
for value in duplicates_list:
	print(str(duplicates[value]) + "\t" + value + "\t" + geolite2.lookup(value).country);
