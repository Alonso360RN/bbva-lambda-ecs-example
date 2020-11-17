import boto3
import json
import os

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ["TABLE_NAME"])
    table.delete_item(Key = {
        "id": event["pathParameters"]["character-id"]
    })

    return {
        "statusCode": 200,
         "headers": {
            "Access-Control-Allow-Origin": "*"
        }
    }