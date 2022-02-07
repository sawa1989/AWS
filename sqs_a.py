import json
import boto3


def lambda_handler(event, context):
    sqs_client = boto3.client(
        service_name='sqs',
        region_name='us-east-1'
    )

    response = sqs_client.send_message(
        QueueUrl='arn_ctrlc_ctrlv',
        MessageBody='from sqs_a (lambda) '
    )

    print(json.dumps(response))
    return json.dumps(response)
