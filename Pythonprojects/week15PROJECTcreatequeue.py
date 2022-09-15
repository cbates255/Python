import boto3

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='week15project',
)
print('The queue has been created')