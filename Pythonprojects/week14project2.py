import boto3
dynamodb=boto3.client("dynamodb")

dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Player',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'Number',
            'AttributeType': 'N',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Player',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Number',
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='Player_list',
)