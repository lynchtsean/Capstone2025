def generate_response(message):
    """
    Generates a response to the user's guitar-related message.
    You can expand this with more logic, database calls, or ML models.
    """
    message = message.lower()

    if "chord" in message:
        return "Sure! A basic G chord looks like this: G - B - D."
    elif "tune" in message or "tuning" in message:
        return "Standard guitar tuning from lowest to highest string is: E A D G B E."
    elif "practice" in message:
        return "Practice 20 minutes daily. Start with scales and transition into chord changes."
    elif "strumming" in message:
        return "Try down-down-up-up-down-up as a beginner strumming pattern."
    elif "scale" in message:
        return "The pentatonic scale is a great place to start: A - C - D - E - G."
    elif "french" in message or "français" in message:
        return "Désolé, la version française arrive bientôt! 🎸"
    else:
        return "I'm here to help with chords, tuning, practice tips, and more. Ask away!"

def lambda_handler(event, context):
    """
    AWS Lambda handler function triggered via API Gateway.
    Expects JSON input with 'message' and optional 'userId'.
    """
    try:
        body = json.loads(event.get("body", "{}"))
        user_message = body.get("message", "")

        if not user_message:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing 'message' in request body."})
            }

        reply = generate_response(user_message)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",  # CORS support
            },
            "body": json.dumps({"reply": reply})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"error": f"Internal server error: {str(e)}"})
        }
