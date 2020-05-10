import json
import boto3

ec2 = boto3.client('ec2')
sns = boto3.client('sns')


def lambda_handler(event, context):
    # TODO implement
    #print(event)
    ec2_instance_id=event['detail']['instance-id']
    
    # Put Logic
    tag_response= ec2.describe_tags(
    Filters=[
        {
            'Name': 'resource-id',
            'Values':[ec2_instance_id],
        },
    ],
    )

    alltags=tag_response['Tags']
    
    flag='STOP'
    for item in alltags:
        print(item['Key'])
        if item['Key']=='SPECIAL_EXCEPTION':
            flag='DONT_STOP'
            break
            
    print(flag)    
    
    # Decision Making
    
    if flag=='STOP':
        ec2.stop_instances(InstanceIds=[ec2_instance_id])
        snsarn="arn:aws:sns:us-east-1:123456789123:email-SNS-topic"
        errormsg="EC2 "+ ec2_instance_id + " stopped"
        snsresponse=sns.publish(TopicArn=snsarn,
                                Message=errormsg,
                                Subject="EC2 Violated Company Policy")
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
