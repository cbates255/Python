#Practice creating an S3 bucket with boto3

import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('testing784512')
response = bucket.create(
    ACL='public-read',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    },
)

print(response)