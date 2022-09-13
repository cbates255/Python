#Code to wait for table status to go active before printing 'table active'

from msilib import Table
import boto3
db=boto3.resource('dynamodb')

db.create_table(TableName='Movies',)

print('Table status:', db.table_status)

print('Waiting for', db.name, 'to complete creating...')
db.meta.client.get_waiter('table_exists').wait(TableName='Movies')
print('Table status:', db.Table('Movies').table_status)