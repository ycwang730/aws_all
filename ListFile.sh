#!/bin/bash

# $RANDOM

username=$1
password=$2


echo "Your username is $username"

declare condition_flag=0
declare condition_flag_2=0

bucket_name="yinchiehwang-assignment5"
#echo $bucket_name
list_key_command=`aws s3 ls s3://$bucket_name`
echo -e "$list_key_command\n" > username_result_3.txt 2>&1


while read line
do
	all_username=`echo $line | rev | cut -d' ' -f 1 | rev`
	#echo $all_username
	echo $all_username >> username_list_3.txt

done < "username_result_3.txt"

while read line
do
	if [[ $username == $line ]]
	then
		echo "Username matches"
		condition_flag=1
		username_bucket_to_check=`aws s3 ls | cut -d' ' -f 3`
		echo -e "$username_bucket_to_check\n" >> username_bucket_check_2.txt
		download_password=`aws s3 cp s3://$bucket_name/$username $username`

	
	fi
done < "username_list_3.txt"

if [[ $condition_flag -ne 1 ]]
then
	echo "Username does not match"
else
	while read line
	do
		if [[ $password == $line ]]
		then
			echo "Password matches"
			condition_flag_2=1
		else
			echo "Password does not match"
		fi
	done < "$username"
fi

if [[ $condition_flag_2 -eq 1 ]]
then
	while read line
	do
		if [[ $line =~ $username ]]
		then
			bucket_to_handle=$line
		fi
	done < "username_bucket_check_2.txt"
	echo "Your bucket name is $bucket_to_handle"
	echo "List your files in the bucket"
	echo ""
	list_file_bucket=`aws s3 ls s3://$bucket_to_handle/ | rev | cut -d ' ' -f 1 | rev`
	echo $list_file_bucket
	delete_file_3=`rm username_bucket_check_2.txt`
fi


delete_file_2=`rm username_list_3.txt`
