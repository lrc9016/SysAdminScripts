#!/bin/bash


function startupProcs {
	#Create Processes and print their ids.
	./APM1 $1 &
	pid1=$!
	echo "Process 1: ${pid1}, Started!"
	./APM1 $1 &
	pid2=$!
	echo "Process 2: ${pid2}, Started!"
	./APM1 $1 &
	pid3=$!
	echo "Process 3: ${pid3}, Started!"
	./APM1 $1 &
	pid4=$!
	echo "Process 4: ${pid4}, Started!"
	./APM1 $1 &
	pid5=$!
	echo "Process 5: ${pid5}, Started!"
	./APM1 $1 &
	pid6=$!
	echo "Process 6: ${pid6}, Started!"
	#Collect Interface Data
	ifstat -a -d 1
	#Array of Processes
	procIDs=("$pid1" "$pid2" "$pid3" "$pid4" "$pid5" "$pid6")
}

function collectSystemMetrics {

	local hardDiskReads=$(iostat sda | tail -2 | head -1 |awk -F ' ' '{print $3}')
 	
	local hardDiskUtil=$(df | grep centos-root | awk -F ' ' '{print $3}')	
	local ifstatLine=$(ifstat | grep ens192)
	local dxRate=$(echo $ifstatLine | awk '{print $7}')
	local txRate=$(echo $ifstatLine | awk '{print $9}')
	
	if [[ "$dxRate" == *"K"* ]]; then
		dxRate=${dxRate::-1}
		dxRate=$(($dxRate*1000))	
	fi
	if [[ "$txRate" == *"K"* ]]; then
                txRate=${txRate::-1}    
                txRate=$(($txRate*1000))
        fi	
	dxRate=$(($dxRate/1000))
	txRate=$(($txRate/1000))
			
	hardDiskUtil=$(($hardDiskUtil/1000000))
	echo "$TIMER,$dxRate,$txRate,$hardDiskReads,$hardDiskUtil" >> $sysFile				
}

function collectProcessMetrics {
	#create the files (in the main loop "run")
	local num=1
	for pid in "${procIDs[@]}"
	do
		local CPU=$(ps -aux | grep \spid\s | awk '{print $3}')
		local MEMORY=$(ps -aux | grep \spid\s | awk '{print $4}')
		#write to file with seconds
		procFile="APM"$num"_metrics.csv"
		echo "$TIMER,$CPU,$MEMORY" >> $procFile
		num=$(($num+1))
	done
}


function cleanup(){
	#Kill all processes (including ifstat)
	kill -9 $pid1
	kill -9 $pid2
	kill -9 $pid3
	kill -9 $pid4
	kill -9 $pid5
	kill -9 $pid6
	pkill -f -9 "ifstat"
	exit $?
}


function run {
	#call cleanup when exited prematurely
	trap cleanup SIGINT
	#Create Files to Write to
	sysFile="system_metrics.csv"   
        > $sysFile
	> "APM1_metrics.csv"
	> "APM2_metrics.csv"
	> "APM3_metrics.csv"
	> "APM4_metrics.csv"
	> "APM5_metrics.csv"
	> "APM6_metrics.csv"
	#Timer
	TIMER=0
		while true ;
		do
			sleep 1;
				
			TIMER=$(($TIMER+1))
			# 900 for 15 mins
			if [[ $duration -ge 900 ]]; then
				cleanup
			fi
			duration=$TIMER
			collectSystemMetrics
			if [[ $(($duration%5)) == 0 ]]; then
				collectProcessMetrics
			fi
		done
}

startupProcs 192.168.203.116 #this may need to be changed to 192.168.122.1, was origially 8.8.8.8
run



