#Create a list and add services to list, then count the list. Work with the list
#by amending items, then print the list. 

from operator import add
from time import sleep


AWSservices = []

AWSservices.append("Ec2")
AWSservices.append("ECS")
AWSservices.append("DynamoDB")
AWSservices.append("S3")
AWSservices.append("Lambda")

#Add 5 services to the list
print (*AWSservices)
sleep(1)
print("The number of services in this list is:", len(AWSservices))

sleep(1)

print ("Removing 2 items from the list...")
sleep(2)
print ("Still computing this complex code...")
sleep(3)

#Delete the first 2 services from the list
del AWSservices[0]
del AWSservices[0]

print (*AWSservices)
sleep(1)
print ("The length of the list is now:", len(AWSservices))