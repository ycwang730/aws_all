# -*- coding: utf-8 -*-
import string
import os,sys
import argparse
import boto
from boto.s3.key import Key


#print(sys.argv)
key_name_match = sys.argv[1]
value_number_match = sys.argv[2]
file_name = sys.argv[3]
path_on_local = sys.argv[4]

s3=boto.connect_s3()
bucketlist=s3.get_all_buckets()

bucketname_of_mine='yinchieh-assignment4'
bucket=s3.get_bucket(bucketname_of_mine)

for key in bucket.list():
    name_to_check = str(key.name)
    name_to_check_user = str(key_name_match)
    password_to_check = key.get_contents_as_string()
    password_to_check_user = str(value_number_match)
    
    print 'username you inserted : ' + key_name_match
    
    #print password_to_check
    print 'password you inserted : ' + password_to_check_user
    
    result1 = name_to_check == name_to_check_user
    result2 = password_to_check == password_to_check_user
    
    if result1 & result2 == True:
        print 'username and password match database'
    
        for bucket_name in bucketlist:
            bucket_store_to_check = str(bucket_name).split(":",1)[1].strip()[:-1]
            if name_to_check in bucket_store_to_check:
                bucket_to_download=s3.get_bucket(bucket_store_to_check)
                bucket_list_to_download = bucket_to_download.list()
                #print bucket_list_to_download
                
                for keystring in bucket_list_to_download:
                    key_to_check = str(keystring).split(",",1)[1].strip()[:-1]
                    
                    #print key_to_check
                    if key_to_check == file_name:
                        if os.path.exists(path_on_local+file_name):
                            print 'File exists at your local machine'
                            sys.exit()
                        if not os.path.exists(path_on_local+file_name):
                            print 'Download file ' + file_name
                            keystring.get_contents_to_filename(path_on_local+file_name)
                            sys.exit()
                print 'File not found'

    else:
        print 'username and password do not match database'
