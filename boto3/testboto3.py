import boto3

ec2 = boto3.resource('ec2')
filter = [{'Name': 'tag:testing', 'Values': ['test']}]
response = ec2.instances.filter(Filters=filter)
ec2.instances.filter(Filters=filter).terminate()

print('The instance ', *response, ' has been terminated!')