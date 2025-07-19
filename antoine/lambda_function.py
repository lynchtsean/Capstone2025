import boto3

def lambda_handler(event, context):
    # 🎸 My reminder message
    message = "🎸 Hey there! It's time to practice your guitar."

    # 📨 Set up SNS client
    sns = boto3.client('sns', region_name='us-east-1')

    # 🔗 Replace this with your real SNS topic ARN
    topic_arn = "arn:aws:sns:us-east-1:909889355275:GuitarReminders"


    try:
        # 📤 Send the reminder via SNS
        response = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Guitar Practice Reminder"
        )

        print("Reminder sent! Message ID:", response['MessageId'])

        return {
            'statusCode': 200,
            'body': 'Reminder successfully sent.'
        }

    except Exception as e:
        print("Error sending reminder:", str(e))
        return {
            'statusCode': 500,
            'body': f'Error sending reminder: {str(e)}'
        }
