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
        eventname = detail['eventName']
        arn = detail['userIdentity']['arn']
        principal = detail['userIdentity']['principalId']
        user_type = detail['userIdentity']['type']

        if user_type == 'IAMUser':
            user = detail['userIdentity']['userName']
        else:
            user = principal.split(': ')[1]

        print('arn: ' + arn)
        print('principalId: ' + principal)
        print('region: ' + region)
        print('eventName: ' + eventname)
        print('detail: ' + str(detail))
        print('user: ' + user)

        