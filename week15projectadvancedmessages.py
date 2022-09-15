import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    message = event['Records'][0]['body']
    print('The message is: ' + message)

    sns.publish(
    Message='In case you weren\'t aware, ' + message,
    Subject='Week 15 project!',
    TopicArn='arn:aws:sns:us-east-1:913213447178:week15sns'
    )