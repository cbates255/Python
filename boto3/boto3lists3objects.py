import boto3

s3_resource=boto3.client("s3")
#s3_resource.list_objects(Bucket='testing784512')
#This will provide a list of the objects in the bucket.

objects=s3_resource.list_objects(Bucket='testing784512')['Contents']
print(len(objects))
#The above gives the number of objects in the bucket. 

