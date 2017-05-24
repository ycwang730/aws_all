#!/bin/bash

echo ""
echo Attempting to confirm Tomcat is installed on:$1
echo ""

isinst=$(wget -t 1 --timeout=1 -q -O /dev/stdout http://$1:8080|head -n 2|grep -o 'Apache')

if [ "$isinst" != "Apache" ]
then
	echo trying again with longer timeout
	isinst=$(wget -t 3 --timeout=3 -q -O /dev/stdout http://$1:8080|head -n 2|grep -o "Apache")
fi

if [ "$isinst" == "Apache" ]
then
	echo 'Tomcat installed'
else
	echo 'not confirmed'
fi
