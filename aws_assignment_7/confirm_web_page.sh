#!/bin/bash

echo Attempting to confirm webpage MyPage.html is set up on:$1
echo ""

isinst=$(wget -t 1 --timeout=1 -q -O /dev/stdout http://$1:8080/MyWebApp/MyPage.html|grep -o 'hello world!')

if [ "$isinst" != "hello world!" ]
then
	echo trying again with longer timeout
	isinst=$(wget -t 3 --timeout=3 -q -O /dev/stdout http://$1:8080/MyWebApp/MyPage.html|grep -o "hello world!")
fi

if [ "$isinst" == "hello world!" ]
then
	echo 'Webpage MyPage.html set up!'
else
	echo 'not confirmed'
fi
