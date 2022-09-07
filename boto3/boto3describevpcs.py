import boto3
vpc=boto3.client("ec2")

x=vpc.describe_vpcs()
print(len(x))
print(x)