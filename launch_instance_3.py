import boto
import boto.vpc
region='us-west-1'

ec2=boto.ec2.connect_to_region(region)

for v in ec2.get_all_volumes():
    print v

for v in ec2.get_all_volumes():
    print v.status
