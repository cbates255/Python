import boto3
import pprint
sqs=boto3.client("sqs")

response = sqs.receive_message(
    QueueUrl='https://queue.amazonaws.com/913213447178/Callqueue',
)

messages=response['Messages']
for message in messages:
    data=message['Body']
    print(data)