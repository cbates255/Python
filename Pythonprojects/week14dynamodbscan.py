from urllib import response
from boto3.dynamodb.conditions import Key,Attr
import boto3
dynamodb=boto3.resource("dynamodb")
table=dynamodb.Table('Player_list')

response=table.scan(
    FilterExpression=Attr('Number').gte(5)
)
print(response)