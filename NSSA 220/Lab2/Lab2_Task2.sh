#!/bin/bash
#task two of lab two

letter_writer () {
	WELCOME_PATH="/home/$USERNAME/Documents/welcome.txt"
	touch $WELCOME_PATH
	echo "Dear $FIRST_NAME," >> $WELCOME_PATH
	echo >> $WELCOME_PATH
	echo "Welcome to Initech Corporation! We're so happy to have you in the $DEPARTMENT Department as a $JOB_TITLE. Please" >> $WELCOME_PATH
	echo "don't forget to complete your TPS Reports in a timely manner." >> $WELCOME_PATH
	echo >> $WELCOME_PATH
	echo "Sincerely," >> $WELCOME_PATH
	echo >> $WELCOME_PATH
	echo "Bill Lumbergh" >> $WELCOME_PATH
}

file_system_writer () {
	mkdir /home/$USERNAME/Desktop
	mkdir /home/$USERNAME/Documents
	mkdir /home/$USERNAME/Downloads
	mkdir /home/$USERNAME/Pictures
	cp ackbar.jpg /home/$USERNAME/Pictures
}

permission_editor () {
	chown -R $USERNAME:$USERNAME /home/$USERNAME
	chmod 0444 /home/$USERNAME/Documents/welcome.txt
	
}

RESPONSE="y"

while [[ "$RESPONSE" == "y" ]]
do
	read -p "Username: " USERNAME
	read -p "Full Name: " FIRST_NAME LAST_NAME
	read -p "Department: " DEPARTMENT
	read -p "Job Title: " JOB_TITLE
	echo
	useradd $USERNAME -m -d /home/$USERNAME
	file_system_writer
	letter_writer
	permission_editor
	echo "User $USERNAME added!"
	echo
	ls -lR /home/$USERNAME
	echo
	cat /home/$USERNAME/Documents/welcome.txt
	echo
	read -p "Would you like to add another user? (y/n): " RESPONSE
done

