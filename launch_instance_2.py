import boto
import boto.vpc
region='us-west-1'
ec2=boto.ec2.connect_to_region(region)

instlist=ec2.get_all_instances()
print instlist[1]
res=instlist[1]

inst=res.instances[0]
print inst.state
print inst.id
