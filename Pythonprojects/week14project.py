#Script to stop specified running EC2 instances.
import boto3

ec2=boto3.client("ec2")

response = ec2.stop_instances(
    InstanceIds=[
        'i-02eb2530c37e40495',
        'i-060e7f819517642b2',
        'i-00d0f7b5348107e93'
    ],
)