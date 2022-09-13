import boto3
import datetime

q = boto3.client('sqs')


def lambda_handler(event, context):
    stamp = datetime.datetime.now()
    current = stamp.strftime("%Y-%m-%d %H:%M:%S")
    response = q.list_queues()
    queueurl = response['QueueUrls']
    print('Sending message...')


    message = q.send_message(
    QueueUrl=queueurl[0]
    MessageBody='The current date and time is' + current
)

    print('The message has been sent to', queueurl)

