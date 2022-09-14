#Puts a tag on all API calls to runinstances, create volume
# /snapshot/image

import json
import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    print('Event: ' + str(event))
    print(json.dumps(event))

    ids = []

    try:
        region = event['region']
        detail = event['detail']
