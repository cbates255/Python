import boto3
db = boto3.client('dynamodb')

response = db.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Date',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'MessageID',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'MessageBody',
            'AttributeType': 'S'
        },
    ],
    TableName='15projectTABLE',
    KeySchema=[
        {
            'AttributeName': 'Date',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'MessageID',
            'KeyType': 'RANGE'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    },
    TableClass='STANDARD',
)