import boto3

sqs=boto3.client("sqs")

response = sqs.send_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/913213447178/Callqueue',
    MessageBody='Message sent from Python',
)

print('Message sent')