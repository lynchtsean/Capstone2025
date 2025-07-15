import json

def detect_intent(message):
    message = message.lower()
    if "chord" in message or "scale" in message:
        return "chord"
    elif "practice" in message or "tip" in message:
        return "practice"
    elif "song" in message or "recommend" in message:
        return "song"
    elif "challenge" in message:
        return "challenge"
    else:
        return "general"

def generate_response(message, user_id="user"):
    intent = detect_intent(message)

    if intent == "chord":
        return f"🎵 Hey {user_id}, which chord would you like to learn? G major, D minor, or C major?"
    elif intent == "practice":
        return f"💪 Practice tip for you, {user_id}: Start slow and use a metronome. Accuracy beats speed!"
    elif intent == "song":
        return f"🎶 {user_id}, try playing 'Wonderwall' by Oasis or 'Wish You Were Here' by Pink Floyd — great beginner songs!"
    elif intent == "challenge":
        return f"🔥 Challenge for you, {user_id}: Try playing the minor pentatonic scale in all positions this week!"
    else:
        return f"🤖 Hi {user_id}! I can help with chords, song suggestions, or practice tips. What would you like help with?"

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        message = body.get("message", "")
        user_id = body.get("userId", "guitarist")

        if not message:
            return {
                "statusCode": 400,
                "headers": { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
                "body": json.dumps({"reply": "Please provide a message!"})
            }

        reply_text = generate_response(message, user_id)

        return {
            "statusCode": 200,
            "headers": { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
            "body": json.dumps({"reply": reply_text})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
            "body": json.dumps({"reply": f"Error: {str(e)}"})
        }
