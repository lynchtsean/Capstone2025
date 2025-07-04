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
