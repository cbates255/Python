#Script to stop specified running EC2 instances.
import boto3

ec2=boto3.resource("ec2")


ec2_filter=[{'Name': 'tag:Environment', 'Values': ['Dev']}, {'Name': 'instance-state-name', 'Values': ['running']}]

ec2.instances.filter(Filters=ec2_filter).stop()