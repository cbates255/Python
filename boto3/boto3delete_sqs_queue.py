import boto3
import pprint
sqs=boto3.client("sqs")

response=sqs.delete_queue(
    QueueUrl='https://queue.amazonaws.com/913213447178/Callqueue'
)

print('Queue deleted')