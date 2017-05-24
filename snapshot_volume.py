import os
import sys
import boto.vpc


vol_id = sys.argv[1]
print "The volume you want to create snapshot is " + vol_id

region='us-west-1'
ec2=boto.ec2.connect_to_region(region)

all_vol=ec2.get_all_volumes()

#print all_vol[1]
i = 0
length = len(all_vol)

for i in range(length):
    if str('Volume:'+ vol_id) == str(all_vol[i]):
        vol = all_vol[i]
    i = i + 1

print ''
print "create snapshot for this volume: " + str(vol)
snapshot_info = vol.create_snapshot('ucsc-aws-class')

print snapshot_info

