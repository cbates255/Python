import boto3

sqs=boto3.client("sqs")

response = sqs.create_queue(
    QueueName='Callqueue',
)

print('Queue created')