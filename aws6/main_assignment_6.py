import launch_instance
from launch_instance import *
dir(launch_instance)


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


#start to create volume
vol=con.create_volume(2,azone)
print vol
print "Wait the volume to be ready"
time.sleep(10)
vol.attach(inst.id,'/dev/sdf')

dns_name=inst.public_dns_name
print "Instance DNS is " + dns_name
