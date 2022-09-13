import boto3
import time

q = boto3.client('sqs')

response = q.list_queues()
queueurl = response['QueueUrls']
print('Sending message...')

message = q.send_message(
    QueueUrl=queueurl,
    MessageBody='Week 15 project message',
)

print('The message has been sent to', queueurl)

