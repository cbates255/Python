from ast import Del
import boto3
#Delete objects from S3 bucket.
s3=boto3.client("s3")
s3.delete_object(Bucket='testing784512', Key='Listlab.py')

#Delete multiple objects

import glob
files=glob.glob('*.py')

response = s3.delete_objects(
    Bucket='testing784512',
    Delete={
        'Objects': [
            {
                'Key': 'bio.py',
            },
        ],
    },
)

