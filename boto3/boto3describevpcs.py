from cgitb import handler
import boto3
vpc=boto3.client("ec2")

x=vpc.describe_vpcs()

vpcnumber=x["Vpcs"]

#get vpc id out 

for i in vpcnumber:
    print(i["VpcId"])
