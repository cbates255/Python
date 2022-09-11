import boto3

ebs=boto3.client('ec2')

ebs.delete_snapshot(SnapshotId='snap-0c53f209f9feeff35')

print('Snapshot has been successfully deleted')