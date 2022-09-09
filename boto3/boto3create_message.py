import boto3

sqs=boto3.client("sqs")

response = sqs.send_message(
    QueueUrl='string',
    MessageBody='Message sent from Python',
)