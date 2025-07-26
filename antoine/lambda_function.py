import boto3

def lambda_handler(event, context):
    phone = event.get("phone")     # from your Flask form
    message = event.get("message") # also from your Flask form

    sns = boto3.client('sns', region_name='us-east-1')

    response = sns.publish(
        PhoneNumber=phone,
        Message=message
    )

    print("Reminder sent! Message ID:", response['MessageId'])

    return {
        'statusCode': 200,
        'body': 'Reminder successfully sent.'
    }
