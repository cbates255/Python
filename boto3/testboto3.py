import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('15projectTABLE')

response = table.delete()
print(response)