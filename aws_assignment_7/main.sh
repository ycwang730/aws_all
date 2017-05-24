#!/bin/bash

echo "Starting"
echo ""
keyfile=assignment6
keypath=/home/npc/


ipandinstid=$(python start.py)
ipandinstid2=$(python start.py)
ipandinstid3=$(python start.py)

ipaddr=$(echo $ipandinstid | cut -f 1 -d ,)
instid=$(echo $ipandinstid | cut -f 2 -d ,)
ipaddr2=$(echo $ipandinstid2 | cut -f 1 -d ,)
instid2=$(echo $ipandinstid2 | cut -f 2 -d ,)
ipaddr3=$(echo $ipandinstid3 | cut -f 1 -d ,)
instid3=$(echo $ipandinstid3 | cut -f 2 -d ,)


echo $instid
echo $instid2
echo $instid3
echo ""
echo ip=$ipaddr
echo ip=$ipaddr2
echo ip=$ipaddr3
echo ""

rtn=$(python install.py $ipaddr $keyfile $keypath)
rtn2=$(python install.py $ipaddr2 $keyfile $keypath)
rtn3=$(python install.py $ipaddr3 $keyfile $keypath)

echo ""
echo ""
slp=10
echo sleep $slp seconds
sleep $slp
echo wake up

echo ""
echo confirming Tomcat installation on $ipaddr
bash ./confirm.sh $ipaddr
echo ""
echo ""
echo ""
echo confirming Tomcat installation on $ipaddr2
bash ./confirm.sh $ipaddr2
echo ""
echo ""
echo ""
echo confirming Tomcat installation on $ipaddr3
bash ./confirm.sh $ipaddr3

echo ""
echo "Start to set up webpage on those instances"
echo ""

webin=$(python webinit.py $ipaddr)
webin2=$(python webinit.py $ipaddr2)
webin3=$(python webinit.py $ipaddr3)

echo ""
echo sleep $slp seconds
sleep $slp
echo wake up

echo ""
echo ""
echo "Start to confirm if the webpage has been set up"

echo "confirming the webpage existence on $ipaddr"
bash ./confirm_web_page.sh $ipaddr
echo ""
echo ""
echo "confirming the webpage existence on $ipaddr2"
bash ./confirm_web_page.sh $ipaddr2
echo ""
echo ""
echo "confirming the webpage existence on $ipaddr3"
bash ./confirm_web_page.sh $ipaddr3
echo ""

echo ""
new_slp=60
echo sleep $new_slp seconds
sleep $new_slp
echo wake up

echo ""
echo "Start to terminate instances"
echo ""

tima=$(python terminate.py $instid)
tima2=$(python terminate.py $instid2)
tima3=$(python terminate.py $instid3)

echo ""
echo "Finish all terminations"
