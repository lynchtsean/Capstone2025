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
    
def save_subscribers(subscribers):
    try:
        json_data = json.dumps(subscribers)
        s3.put_object(Bucket=BUCKET_NAME, Key=FILE_KEY, Body=json_data)
        print("subscribers.json updated successfully in S3.")
    except ClientError as e:
        print(f"Error uploading subscribers.json: {e}")

