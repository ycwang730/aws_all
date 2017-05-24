#!/bin/bash

# $RANDOM

username=$1
password=$2
email_address=$3

declare condition_flag=0

echo -e $password > $username 2>&1

bucket_name="yinchiehwang-assignment5"
#echo $bucket_name
list_key_command=`aws s3 ls s3://$bucket_name`
echo -e "$list_key_command\n" > username_result_2.txt 2>&1


while read line
do
	all_username=`echo $line | rev | cut -d' ' -f 1 | rev`
	#echo $all_username
	echo $all_username >> username_list.txt

done < "username_result_2.txt"

while read line
do
	if [[ $username == $line ]]
	then
		echo "User already exists"
		condition_flag=1
		delete_file=`rm username_list.txt`
		exit
	fi
done < "username_list.txt"

if [[ $condition_flag -ne 1 ]]
then
	create_new_username=`aws s3 cp $username s3://$bucket_name/`
	echo "Create new username $username"
	user_bucket="$username-$RANDOM-$RANDOM"
	echo $user_bucket
	create_new_user_bucket=`aws s3 mb s3://$user_bucket/ --region us-west-1`
	echo "Create new bucket for $username"
	echo $create_new_user_bucket
fi

delete_file_2=`rm username_list.txt`
