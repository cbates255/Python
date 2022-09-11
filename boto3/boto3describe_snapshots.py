import boto3

ebs=boto3.client('ec2')

ebs.describe_snapshots()
