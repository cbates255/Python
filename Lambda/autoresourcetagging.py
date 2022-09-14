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

        if not detail['responseElements']:
            print('No responseElements found')
            if detail['errorCode']:
                print('errorCode: ' + detail['errorCode'])
            if detail['errorMessage']:
                print('errorMessage: ' + detail['errorMessage'])
            return False

        if eventname == 'CreateVolume':
            ids.append(detail['responseElements']['volumeId'])
            print(ids)

        elif eventname == 'RunInstances':
            items = detail['responseElements']['instancesSet']['items']
            for item in items:
                ids.append(item['instanceId'])
            print(ids)
            print('number of instances: ' + str(len(ids)))

            base = ec2.instances.filter(InstanceIds=ids)

            for instance in base:
                for vol in instance.volumes.all():
                    ids.append(vol.id)
                for eni in instance.network_interfaces:
                    ids.append(eni.id)

        elif eventname == 'CreateImage':
            ids.append(detail['responseElements']['imageId'])
            print(ids)

        elif