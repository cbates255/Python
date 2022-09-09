import boto3

sqs=boto3.client("sqs")

def create_queue(sqs, QueueName):
    response = sqs.create_queue(
        QueueName=QueueName
)

print('Queue created')

def get_queue_url(sqs, Queuename):
    response = sqs.get_queue_url(
        QueueName=Queuename,
)
    url=response['QueueUrl']
    print(url)
    return url

if __name__=="__main__":
    sqs=boto3.client('sqs')
    QN='gold_from_function-2'
    create_queue(sqs, QN)
    get_queue_url(sqs, QN)