import os
import time
import boto
import boto.vpc

def launch_instance(ami='ami-165a0876',instance_type='t2.micro',key_name='assignment6',security_group_id='sg-b226a7d5',vpcid='vpc-b316c4d7',ssh_port=22,cidr='0.0.0.0/0',tag='test_6',user_data=None,region='us-west-1'):
 #create connection to ec2
 ec2=boto.ec2.connect_to_region(region)
 vpccon = boto.vpc.connect_to_region(region)

 #get vpccon
 vpc=vpccon.get_all_vpcs(vpc_ids=[vpcid])[0]
 sn=vpccon.get_all_subnets(filters={'vpcId':[vpcid]})
 sn1=sn[0]
 try:
     key=ec2.get_all_key_pairs(keynames=[key_name])[0]
 except ec2.ResponseError, e:
     if e.code == 'InvalidKeyPair.NotFound':
         print 'Creating ketpair: %s' %key_anme
         key=ec2.create_key_pair(key_name)
         key.save(key_dir)
     else:
         raise

 try:
     security_group=ec2.get_all_security_groups(group_ids=[security_group_id])[0]
 except ec2.ResponseError, e:
     if e.code == 'InvalidGroup.NotFound':
         print 'Creating Security Group: %s' %security_group_id
         security_group=ec2.create_security_group('ZcatSecurityGroup','A group that allows SSH access')
     else:
         print 'Security group error:%s'%e.message
         raise
 try:
     security_group.authorize('tcp',22,22,cidr)
 except ec2.ResponseError,e:
     if e.code=='InvalidPermission.Duplicate':
         print'Security Group:%s already authorized for ssh' %security_group_id
     else:
         raise

 #start up the instance
 reservation=ec2.run_instances(ami,key_name=key_name,security_group_ids=[security_group.id],subnet_id=sn1.id,instance_type=instance_type,user_data=user_data)
 instance=reservation.instances[0]
 print 'waiting for instance'
 while instance.state != 'running':
     print '.'
     time.sleep(5)
     instance.update()
 print 'done'
 return(instance, reservation)

