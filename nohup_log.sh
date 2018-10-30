#!/bin/bash
logFileName=$1
maxLines=$2
function doRotate()
{
	rm $logFileName'.10' 2> /dev/null
	mv $logFileName'.9' $logFileName'.10' 2> /dev/null
	mv $logFileName'.8' $logFileName'.9' 2> /dev/null
	mv $logFileName'.7' $logFileName'.8' 2> /dev/null
	mv $logFileName'.6' $logFileName'.7' 2> /dev/null
	mv $logFileName'.5' $logFileName'.6' 2> /dev/null
	mv $logFileName'.4' $logFileName'.5' 2> /dev/null
	mv $logFileName'.3' $logFileName'.4' 2> /dev/null
	mv $logFileName'.2' $logFileName'.3' 2> /dev/null
	mv $logFileName'.1' $logFileName'.2' 2> /dev/null
	mv $logFileName $logFileName'.1' 2> /dev/null
	touch $logFileName
}

######################################################
#Uncomment the below block if you want to use the path
#to the log file relative to this script
#rather then where its called from
######################################################
#SOURCE="${BASH_SOURCE[0]}"
#while [ -h "$SOURCE" ]; do
#  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
#  SOURCE="$(readlink "$SOURCE")"
#  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
#done
#DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
#cd $DIR
######################################################

while read logwrite; do
	echo $logwrite >> $logFileName
	numlines=`cat $logFileName | wc -l`
	if [ "$numlines" -ge "$maxLines" ]
	then
	  doRotate
	fi
done
