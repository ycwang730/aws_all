import os, sys
import launch_instance
from launch_instance import *
dir(launch_instance)


snapshot_id = sys.argv[1]

#launch instance
l=launch_instance()
print l

inst=l[0]
reservation=l[1]

con=inst.connection
print con
print "Instance ID is " + inst.id
azone=inst.placement
print "Region is " + azone

ec2=boto.connect_ec2()
ec2=boto.ec2.connect_to_region('us-west-1')
print ec2

print "The snapshot you want to attach : " + snapshot_id
snap_vol=ec2.create_volume(2, inst.placement, snapshot_id)

print "Wait the attached snapshot to be ready"
time.sleep(10)
print snap_vol
snap_vol.attach(inst.id,'/dev/sdf')

dns_name=inst.public_dns_name
print "Instance DNS is " + dns_name

