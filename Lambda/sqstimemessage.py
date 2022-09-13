import boto3
import datetime

q = boto3.client('sqs')
stamp = datetime.datetime.strftime("%Y-%m-%d %H:%M:%S")
print(stamp)
"""
response = q.list_queues()
queueurl = response['QueueUrls']
print('Sending message...')

message = q.send_message(
    QueueUrl=queueurl,
    MessageBody='The current time is' + stamp
)

print('The message has been sent to', queueurl)
"""
