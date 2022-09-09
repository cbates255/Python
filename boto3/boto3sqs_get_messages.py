import boto3
sqs=boto3.client("sqs")

response = client.receive_message(
    QueueUrl='https://queue.amazonaws.com/913213447178/Callqueue',
)