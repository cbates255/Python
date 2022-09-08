from email.mime import image
import boto3
import pprint
ec2=boto3.client("ec2")

x=ec2.describe_instances()
data=x["Reservations"]

#Reservations, Instances, InstanceId

for i in data:
    t=i["Instances"]
    for o in t:
        ids=o["InstanceId"]
        state=o["State"]
        print(ids,state)