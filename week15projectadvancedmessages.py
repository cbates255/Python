import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    for message in event['Records']['body']:
        print('The message is: ' + message)

    response = sns.publish(
    Message='In case you weren\'t aware, ' + message
    Subject='Week 15 project!',
    TopicArn='arn:aws:sns:us-east-1:913213447178:week15sns'
    )