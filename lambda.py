import json
import boto3

def lambda_handler(event, context):
    # Connect to DynamoDB resource
    client = boto3.resource('dynamodb')
    
    # Create a DynamoDB client for the 'visitorCounter' table
    table = client.Table('visitor_count')
    # increment visitor count for resume.html
    response = table.update_item(
        Key={
            'path': 'resume.html'
        },
        AttributeUpdates={
            'visitor_count': {
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
    
    # get visitor_count from the visitorCount table for resume.html
    response = table.get_item(
        Key={
            'path': 'resume.html'
        }
    )
    visitor_count = response['Item']['visitor_count']
    
    return {
        'statusCode': 200,
        'headers':{
            'Access-Control-Allow-Origin':'*'
        },
        'body': visitor_count
    }
