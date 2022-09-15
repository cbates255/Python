import boto3
db = boto3.client('dynamodb')
import datetime
date=datetime.date.today()

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    id = event['Records'][0]['Sns']['MessageId']

    response = db.put_item(
        Item={
            'Date': {
                'S': str(date),
            },
            'MessageID': {
                'S': id,
            },
            'Message': {
                'S': message,
            },
        },
        ReturnConsumedCapacity='TOTAL',
        TableName='15projectTABLE',
    )

    print(response)