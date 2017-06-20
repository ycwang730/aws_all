import os, sys
import time
import boto
import boto.vpc
import boto.vpc.vpc

def main():
 instance_to_delete=sys.argv[1]
 vol_to_delete=sys.argv[2]
 snapshot_to_delete=sys.argv[3]
 print(sys.argv)

 ec2=boto.connect_ec2()
 ec2=boto.ec2.connect_to_region('us-west-1')
#vpccon = boto.vpc.connect_to_region('us-west-1')

#terminate instance
 print "Terminate the instance"
 ec2.terminate_instances(instance_ids=instance_to_delete)
 time.sleep(60)

#print "Detach the volume"
#ec2.detach_volume(vol_to_delete,instance_id=instance_to_delete)
#time.sleep(5)

 print "Delete the volume"
 ec2.delete_volume(vol_to_delete)
 time.sleep(5)

 print "Delete the snapshot"
 ec2.delete_snapshot(snapshot_to_delete)

if __name__ == "__main__":
 main()
