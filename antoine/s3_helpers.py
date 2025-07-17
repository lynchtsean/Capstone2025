import boto3
import json
from botocore.exceptions import ClientError

# Set up your S3 client
s3 = boto3.client('s3')

# Replace with your actual bucket name
BUCKET_NAME = 'guitar-reminders-2025'
FILE_KEY = 'subscribers.json'

def get_subscribers():
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)
        content = response['Body'].read().decode('utf-8')
        subscribers = json.loads(content)
        return subscribers
    except ClientError as e:
        print(f"Error fetching subscribers.json: {e}")
        return {}
