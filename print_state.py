import boto
import boto.vpc
import boto.vpc.vpc

ec2=boto.connect_ec2()
ec2=boto.ec2.connect_to_region('us-west-1')

instance = ec2.get_all_instance_status()
stat1=instance[0]
stat2=instance[1]
final_stat1=stat1.state_name
final_stat2=stat2.state_name

print stat1
print final_stat1

print stat2
print final_stat2
