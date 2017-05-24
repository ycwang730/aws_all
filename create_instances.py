import boto
import boto.vpc
import boto.vpc.vpc

ec2=boto.connect_ec2()
ec2=boto.ec2.connect_to_region('us-west-1')
vpccon = boto.vpc.connect_to_region('us-west-1')
vpc=vpccon.get_all_vpcs(vpc_ids=['vpc-b316c4d7'])[0]
group=ec2.get_all_security_groups(group_ids=['sg-b226a7d5'])[0]
sn=vpccon.get_all_subnets(filters={'vpcId':['vpc-b316c4d7']})
sn1=sn[0]
sn2=sn[1]

# create/run 2 EC2 instance
ec2.run_instances('ami-165a0876',instance_type='t2.micro',security_group_ids=[group.id],subnet_id=sn1.id,key_name='assignment3')
ec2.run_instances('ami-165a0876',instance_type='t2.micro',security_group_ids=[group.id],subnet_id=sn1.id,key_name='assignment3')

print "create 2 instances"
