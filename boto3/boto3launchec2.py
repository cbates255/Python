import boto3
ec2=boto3.resource("ec2")

ec2.create_instances(InstanceType='t2.micro', ImageId='ami-05fa00d4c63e32376', MinCount=1, MaxCount=1)
    