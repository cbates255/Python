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

def delete_queue(sqs, QueueUrl):
    response=sqs.delete_queue(
    QueueUrl=QueueUrl
)
    print('Queue deleted')

if __name__=="__main__":
    sqs=boto3.client('sqs')
    QN='gold_from_function-3'
    create_queue(sqs, QN)
    qurl=get_queue_url(sqs, QN)
    delete_queue(sqs, qurl)