import boto3
import datetime

q = boto3.client('sqs')


def lambda_handler(event, context):
    stamp = datetime.datetime.now()
    current = stamp.strftime("%Y-%m-%d %H:%M:%S")
    response = q.list_queues()
    url = response['QueueUrls']
    print('Sending message...')

    response = q.send_message(
    QueueUrl=url[0],
    MessageBody='The current date and time is {}.'.format(current),
    )

    print('The message has been sent to', url[0])

