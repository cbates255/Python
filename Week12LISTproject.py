#Create a list and add services to list, then count the list. Work with the list
#by amending items, then print the list. 

from operator import add


AWSservices = []

AWSservices.append("Ec2")
AWSservices.append("ECS")
AWSservices.append("DynamoDB")
AWSservices.append("S3")
AWSservices.append("Lambda")

#Add 5 services to the list
print (*AWSservices)
print("The number of services in this list is:", len(AWSservices))

#Delete the first 2 services from the list
del AWSservices[0]
del AWSservices[0]

print (*AWSservices)