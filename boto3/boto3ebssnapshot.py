import boto3
import pprint

ebs=boto3.client("ec2")

volumes=ebs.describe_volumes()
data=volumes['Volumes']

volumeids=[]

for x in data:
    ids=x['VolumeId']
    volumeids.append(ids)

myid=volumeids[2]

ebs.create_snapshot(VolumeId=myid, Description='Snapshot from base volume')

print('Snapshot has been created')
