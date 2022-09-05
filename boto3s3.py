#Practice creating an S3 bucket with boto3

import boto3
aws_resource = boto3.resource("s3")
bucket = aws_resource.Bucket("testBucket")
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-1'
    },
)

print(response)