import resource
from urllib import response
import boto3

resource = boto3.resource("s3")
resource.buckets.all()
for bucket in resource.buckets.all():
    print(bucket.name)