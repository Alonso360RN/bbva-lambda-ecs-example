import boto3
import json
import os
from datetime import datetime

def lambda_handler(event, context):
    sqs = boto3.client('sqs')
    queue_url = os.environ["QUEUE_URL"]

    today = datetime.now()
    formatted_today = today.strftime("%d/%m/%Y %H:%M:%S")

    records = event["Records"]

    for record in records:
        if record["eventName"] == "INSERT":
            message = {
                "character": record["dynamodb"]["NewImage"]["name"]["S"],
                "time": formatted_today
            }

            jsonMessage = json.dumps(message)
        
            sqs.send_message(QueueUrl = queue_url, MessageBody = jsonMessage)