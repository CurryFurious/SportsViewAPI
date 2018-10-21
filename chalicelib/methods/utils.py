import boto3
import decimal

dynamodb = boto3.resource('dynamodb')

def get_dynamo_table(table_name):
    return dynamodb.Table(table_name)
