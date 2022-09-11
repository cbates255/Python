import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    ec2=boto3.resource("ec2")
    ec2_filter=[{'Name': 'tag:Environment', 'Values': ['Dev']}, {'Name': 'instance-state-name', 'Values': ['running']}]
    ec2.instances.filter(Filters=ec2_filter).stop()
