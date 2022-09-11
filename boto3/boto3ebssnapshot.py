import boto3
import pprint

ebs=boto3.client("ec2")

volumes=ebs.describe_volumes()

pprint.pprint(volumes)