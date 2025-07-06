def lambda_handler(event, context):
    """
    Guitar chatbot Lambda function handler.

    Expects a POST request with JSON body:
    {
        "message": "User's question",
        "userId": "someId"
    }

    Returns:
    {
        "reply": "Bot's response text"
    }
    """
    # Try to parse the body safely
    try:
        body = json.loads(event['body'])
        message = body.get("message", "").lower()
    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"reply": "Invalid request body"})
        }
    
    # Basic chatbot logic
    if "chord" in message:
        reply = "Sure! Here’s a common chord: C major is x32010. Let me know if you want diagrams or other chords!"
    elif "tune" in message or "tuning" in message:
        reply = "To tune your guitar: E A D G B e (standard tuning). You can use a clip-on tuner or an app for best accuracy!"
    elif "song" in message:
        reply = "Here's a classic chord progression: G - D - Em - C. Works for many popular songs!"
    elif "hello" in message or "hi" in message or "hey" in message:
        reply = "Hi there! 🎸 I can help you with chords, tuning, or suggest chords for songs. What would you like to know?"
    else:
        reply = "Sorry, I didn’t understand that. Please ask me about guitar chords, tuning, or songs!"

    # Return JSON response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({
            "reply": reply
        })
    }




import json
import base64
import uuid
import os

s3 = boto3.client('s3')
BUCKET_NAME = os.environ.get("BUCKET_NAME", "my-default-bucket-name")

def lambda_handler(event, context):
    """
    Lambda function to upload an image to S3.

    Expects a POST request with JSON body:
    {
        "image": "base64 string of the image",
        "userId": "someId"
    }

    Returns:
    {
        "message": "Image uploaded successfully",
        "imageUrl": "https://your-bucket-name.s3.amazonaws.com/..."
    }
    """

    # Try to parse and validate input
    try:
        body = json.loads(event['body'])
        image_data = body.get("image", "")
        user_id = body.get("userId", "anonymous")

        if not image_data:
            raise Exception("No image data found.")

        # Decode base64 image
        image_bytes = base64.b64decode(image_data)

        # Generate unique filename
        filename = f"{user_id}/{str(uuid.uuid4())}.jpg"

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=filename,
            Body=image_bytes,
            ContentType="image/jpeg"
        )

        # Create public URL (assumes public-read or presigned setup)
        image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"

        # Success response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "message": "Image uploaded successfully",
                "imageUrl": image_url
            })
        }

    except Exception as e:
        # Error response
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }