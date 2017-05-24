import os, sys
import boto
import boto.vpc
import boto.vpc.vpc
import paramiko
import urllib2

def terminate_instance(instance_id):
    ec2 = boto.connect_ec2()
    ec2=boto.ec2.connect_to_region('us-west-1')
    ec2.terminate_instances(instance_ids=[instance_id])
    
if __name__ == '__main__':
    ins_id=sys.argv[1] 
    sys.stdout.write("terminate instance" + ins_id)
    terminate_all_instance = terminate_instance(ins_id)
    sys.stdout.write("")
    sys.stdout.write("")

