#!/bin/bash
# A small shell.
echo "Hello! This is a program to run homework py."
echo "Please input your user name if you are vip."
read -r user_name
if [ "$user_name" = "mumujun12345" ]
then
	echo "Please input password:"
	read -sr passwd
	if [ "$passwd" = "mumujun12345" ]
	then 
		echo "Running program..."
		sudo python3 /home/parallels/Desktop/mininet/My_folder/test_3.py
		sudo mn -c
	else
		echo "password error! exit..."
		exit
fi
else
	echo "Not vip user! Please wait for initialize."
	sleep 30s
	echo "**-------- 20%"
	sleep 30s
	echo "****------ 40%"
	sleep 30s
	echo "******---- 60%"
	sleep 30s
	echo "********-- 80%"
	sleep 30s
	echo "********** 100%"
	echo "loading..."
	sleep 30s
	echo "Running ..."
	sudo python3 /home/parallels/Desktop/mininet/My_folder/test_3.py
	sudo mn -c
fi


	
