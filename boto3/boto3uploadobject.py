import boto3
#Upload a single file to S3 bucket. 
s3_resource = boto3.client("s3")
s3_resource.upload_file(Bucket = 'testing784512', Filename = 'Listlab.py', Key='testupload')
