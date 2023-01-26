#!/usr/bin/env python3
#Luke Chrampanis   |   9/15/22
#Script 01   |   System Administration

import os;
import time;
#Clear terminal
os.system("clear");
#Initalize significant variables
gatewayIp = "placeholder";
remoteIp = "129.21.3.17";
hostName = "www.google.com";

#Function uses os module to find default gateway then cuts output to just ip address.
def get_default_gateway(input):
	input = os.popen("ip route show | cut -b 13-27 | head -n1 | cut -d ' ' -f 1").read();
	input = input.strip();
	return str(input);

#Function uses os module to ping parameter target and print input is up if ping succeeds, and ping input is down if ping fails.
def test_ping(input):
	result = os.system("ping -c 1 " + input + "> /dev/null 2>&1");
	if result == 0:
		print(input, "is up.");
		return True;
	else:
		print(input, "is down.");
		return False;

#Function Calls
gatewayIp = get_default_gateway(gatewayIp);
#If all return true DNS works, if not DNS is broken

notQuit = True;
while notQuit:
	menu = input("What would you like to test?\nPing Default Gateway (1)\nPing Remote IP (2)\nPing Google.com (3)\nQuit (4)\n\nInput: ");
	print("")
	if (menu == "1"):
		print("Testing Default Gateway...");
		test_ping(gatewayIp);
	elif (menu == "2"):
		print("Testing Remote IP...");
		test_ping(remoteIp);
	elif (menu == "3"):
		print("Testing Google.com...");
		if(test_ping(hostName)):
			print("DNS is functioning.");
		else:
			print("DNS is not functioning.");
	elif (menu == "4"):
		notQuit = False;
	else: print("Input not recognised.");
	time.sleep(1);
	print("");
os.system("clear");
