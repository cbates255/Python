from venv import create
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
    
def create_message(sqs, QueueUrl, message):
    response = sqs.send_message(
    QueueUrl=QueueUrl,
    MessageBody=message,
)

print('Message sent')

def get_message(sqs, QueueUrl):
    response = sqs.receive_message(
    QueueUrl=QueueUrl,
)
    
    out_messages=[]
    
    messages=response['Messages']
    for message in messages:
        data=message['Body']
        print("The uploaded message is: " + data)
        out_messages.append(data)
        return out_messages

if __name__=="__main__":
    sqs=boto3.client('sqs')
    QN='gold_from_function-3'
    create_queue(sqs, QN)
    qurl=get_queue_url(sqs, QN)
    create_message(sqs, qurl, "Learning automation!")
    get_message(sqs, qurl)
    delete_queue(sqs, qurl)
