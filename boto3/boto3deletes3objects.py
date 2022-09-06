import boto3
#Delete objects from S3 bucket.
s3_resource=boto3.client("s3")
s3_resource.delete_object(Bucket='testing784512', Key='Listlab.py')