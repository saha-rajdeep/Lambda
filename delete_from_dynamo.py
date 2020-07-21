import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('People')
    PID=event['PersonID']
    try:
        # TODO: write code...
        response = table.delete_item(
            Key={"PersonID":PID})
        return "Done"
    except:
        raise
