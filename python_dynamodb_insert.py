# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:50:49 2017

@author: saharaj

This lambda program is called by API Gateway POST method to insert
payload into dynamodb (can be replaced with RDS as well).

Sample payload to insert a row in la-lambda-table:
{
    "operation":"create",
    "tableName":"la-lambda-table",
    "payload":{
        "Item":{
            "id":1,
            "fname":"raj",
            "lname":"saha"
        }
    }
}

This is a demo of how lambda can be used by API to do CRUD operations
"""

import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    print("received event:" + json.dumps(event,indent=2))
    
    operation = event['operation']
    
    if 'tableName' in event:
        dynamo = boto3.resource('dynamodb').Table(event['tablename'])
        
    operations = {'create':lambda x:dynamo.put_item(**x)}
    
    if operation in operations:
        return operations[operation](event.get('payload'))
    else:
        raise ValueError('Unrecognized operation "{}"'.format(operation))
        
