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

