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
                'S': date,
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









{
  "Records": [
    {
      "EventSource": "aws:sns",
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:us-east-1:{{{accountId}}}:ExampleTopic",
      "Sns": {
        "Type": "Notification",
        "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
        "TopicArn": "arn:aws:sns:us-east-1:123456789012:ExampleTopic",
        "Subject": "example subject",
        "Message": "example message",
        "Timestamp": "1970-01-01T00:00:00.000Z",
        "SignatureVersion": "1",
        "Signature": "EXAMPLE",
        "SigningCertUrl": "EXAMPLE",
        "UnsubscribeUrl": "EXAMPLE",
        "MessageAttributes": {
          "Test": {
            "Type": "String",
            "Value": "TestString"
          },
          "TestBinary": {
            "Type": "Binary",
            "Value": "TestBinary"
          }
        }
      }
    }
  ]
}