import boto
import boto.vpc
import boto.vpc.vpc

ec2=boto.connect_ec2()
ec2=boto.ec2.connect_to_region('us-west-1')

instance = ec2.get_all_instance_status()

stat1=instance[0]
stat2=instance[1]

instance_id_1=instance[0].id
instance_id_2=instance[1].id


print "Delete" + " " + instance_id_1
print "Delete" + " " + instance_id_2

ec2.terminate_instances(instance_ids=[instance_id_1,instance_id_2])
