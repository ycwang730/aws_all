# -*- coding: utf-8 -*-
import string
import uuid
import sys
import argparse
import boto
from boto.s3.key import Key

print(sys.argv)
key_name = sys.argv[1]
value_number = sys.argv[2]
email_account = sys.argv[3]

#print "save your key name" + sys.argv[1]
#print "save your content" + ' ' + ','.join(value_number)
print "save your username" + ' ' + key_name
print "save your password" + ' ' + value_number
print "save your email" + ' ' + email_account


#parser = argparse.ArgumentParser(description='Process some integers')
#parser.add_argument

s3=boto.connect_s3()

#s3.create_bucket(bucket_name="yinchieh_bucket")
#s3.delete_bucket("yinchieh_bucket")
bucketlist=s3.get_all_buckets()

#for bucket_name in bucketlist:
#        print bucket_name

bucket_name ='yinchieh-assignment4'
bucket=s3.get_bucket(bucket_name)

user_name = Key(bucket)
user_name_check2 = str(key_name)
print user_name_check2

for key in bucket.list():
    if str(key.name) == user_name_check2:
        print 'username already exists'
        sys.exit()
print 'Save username and password successfully'
user_name.key = key_name
user_name.set_contents_from_string(value_number)
newbucketname=key_name + '-' + str(uuid.uuid1())
s3.create_bucket(bucket_name=newbucketname)
print 'Create new bucket : ' + newbucketname
