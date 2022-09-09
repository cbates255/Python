import boto3
import pprint

sqs=boto3.client("sqs")

response = sqs.get_queue_url(
    QueueName='Callqueue',
)
url=response['QueueUrl']
print(url)