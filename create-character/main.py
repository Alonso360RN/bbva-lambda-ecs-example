import boto3
import json
import uuid
import os

def lambda_handler(event, context):
    body = json.loads(event["body"])
    body["id"] = str(uuid.uuid4())

    dynamodb = boto3.resource("dynamodb")
    tableName  = os.environ["TABLE_NAME"]
    table = dynamodb.Table(tableName)
    table.put_item(Item = body)

    response = {
        "statusCode": 201,
        "headers": {
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body)
    }

    return response