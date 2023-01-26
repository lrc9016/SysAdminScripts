#!/usr/bin/env python3
#Luke Chrampanis   |   10/20/22
#Script 03   |   System Administration

import os;
from os.path import exists;
import subprocess;
import time;
#Clear terminal.
os.system("clear");

class colors:
	HEADER = '\033[95m';
	END = '\033[0m';

#Function asks for filepath and returns an array of a boolean of whether the file exists or not and the filepath that was input.
def find_file():
	filename = input("Please input the path to the file (format: \"/home/student/scripts/script03/shortcut.py\")\n\nInput: ");
	print("");
	return((exists(filename), filename));

#Function calls find_file() and then asks for a link name and calls os.system to create a link using the file name, link name, and ln command. Has an output for if the file does not exist.
def create_symbolic_link():
	filename = find_file();
	link_name = input("Please input a name for the link (format: \"script03\")\n\nInput: ");
	if(filename[0]):
		os.system("ln -s " + filename[1] + " " + link_name);
	else:
		print("That file does not exist in that location.");

#Function calls find_file() and then checks if the file name is a link and deletes it if so. Has output for if file is not a link or if file does not exist.
def delete_symbolic_link():
	print("The file is referring to the shortcut you are attempting to delete.");
	filename = find_file();
	if(filename[0]):
		if(os.path.islink(filename[1])):
			os.system("rm " + str(filename[1]));
			print("Deleted: " + str(filename[1]));
		else:
			print("This file is not a link.");
	else:
		print("That file does not exist in that location.")

#Function defines user's home directory and then counts, lists, and lists the target path of each link in the home directory.
def create_summary():
	#Line for clarity
	print("-=-=-=-");
	home_dir = str(subprocess.check_output("ls ~", shell=True)).split("\'")[1].split("\\n");
	del home_dir[-1];
	link_counter = 0;
	links_list = [" "];
	print(colors.HEADER + "Links in Home Directory: " + colors.END);
	for filename in home_dir:
		if(os.path.islink(str(os.path.expanduser("~") + "/" + filename))):
			links_list.append(filename);
			link_counter = link_counter + 1;
			print(filename + ": " + str(subprocess.check_output("readlink " + filename, shell=True)).split("\'")[1].split("\\")[0]);
	print("\n" + colors.HEADER + "Total Links in Home Directory: " + colors.END + str(link_counter));
	print("-=-=-=-");

#Create loop conditional.
notQuit = True;
username = os.getlogin();
pwd = str(subprocess.check_output("pwd", shell=True)).split("\'")[1].split("\\")[0];
#Inform user of their pwd.
print("Hello " + username + ", your present working directory is " + pwd + ".");
print("");
#Menu loop to call functions in easy format for end-user.
while notQuit:
	menu = input("What would you like to do?\nMake a Symbolic Link (1)\nDelete a Symbolic Link (2)\nCreate a Summary (3)\nQuit (4)\n\nInput: ");
	print("");
	if (menu == "1"):
		print("Creating Symbolic Link...\n");
		create_symbolic_link();
	elif (menu == "2"):
		print("Deleting Symbolic Link...\n");
		delete_symbolic_link();
	elif (menu == "3"):
		print("Creating Summary...\n");
		create_summary();
	elif (menu == "4" or menu == "quit"):
		notQuit = False;
	else: print("Input not recognised.");
	time.sleep(1);
	print("");
os.system("clear");

