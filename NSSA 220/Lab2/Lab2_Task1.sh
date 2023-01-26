

#!/bin/bash
#task one of lab two

FILENAME="rand_$1.txt"

num_write () {
	echo "$1" >> "$FILENAME"
}


if [ $1 != 0 ]
then
	touch "$FILENAME"
	if [ -z $2 ]
	then
		for i in $(eval echo {1..$1})
		do
			num_write $(($RANDOM))
		done
		echo "You requested $1 numbers"
	else
		for i in $(eval echo {1..$1})
		do
			num_write $(($2 + $RANDOM % $(($3-$2+1))))
		done
		echo "You requested $1 numbers between $2 and $3"
	fi

	sort -n "$FILENAME" > temp.txt
	SMALLEST_VALUE=$(head -n 1 temp.txt)
	LARGEST_VALUE=$(tail -n 1 temp.txt)
	rm temp.txt

	TOTAL=0
	while read p; do
		TOTAL=$(($TOTAL+$p))
	done <"$FILENAME"
	AVERAGE_VALUE=$(($TOTAL/$1))

	echo "The smallest value generated was $SMALLEST_VALUE"
	echo "The largest value generated was $LARGEST_VALUE"
	echo "The average value generated was $AVERAGE_VALUE"
fi

#eof
