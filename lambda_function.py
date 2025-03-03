import json
import boto3

def lambda_handler(event, context):

    #connect ot DynamoDB resource
    client = boto3.resource('dynamodb')

    # create a DynamoDB client to the visitor table
    table = client.Table('visitor_count')

    response = table.update_item(
        Key={
            'path': 'index.html'
        },
        AttributeUpdates = {
            'visitor_count':{
                'Value':1,
                'Action': 'ADD'
            }
        }
    )

    response = table.get_item(
        Key = {
            'path': 'index.html'
        }
    )

    visitor_count = response['Item']['visitor_count']

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }