import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('People')
    try:
        # TODO: write code...
        response = table.put_item(
          Item=event)
        return "Done"
    except:
        raise
    
