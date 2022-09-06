import boto3
#Upload a single file to S3 bucket. 
#s3_resource = boto3.client("s3")
#s3_resource.upload_file(Bucket = 'testing784512', Filename = 'Listlab.py', Key='testupload')

#Upload multiple files to bucket. 
#import os
import glob
#cwd=os.getcwd()

files=glob.glob('*.py')

for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(Bucket = 'testing784512', Filename = file, Key=file)
