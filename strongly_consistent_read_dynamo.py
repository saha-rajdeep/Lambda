import boto3

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('People')
    PID=event['PersonID']
    try:
        # TODO: write code...
        response = table.get_item(
            Key={"PersonID":PID},
            ConsistentRead=True) #Remove this to turn off Strongly Consistent Reads
        return response
    except:
        raise

