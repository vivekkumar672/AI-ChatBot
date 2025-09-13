# intents/intents.py
from datetime import datetime, date

intents = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hi there! 👋",
    "bye": "Goodbye! Take care!",
    "thanks": "You're welcome 😊",
    "help": "I can help you with Python, AI, or general queries.",
    "who built you" : "i was built by vivek"
}

def check_intent(user_input: str):
    """
    Check if user input matches any predefined intent.
    Simple keyword-based matching.
    """
    user_input = user_input.lower().strip()

    if "time" in user_input:
        now = datetime.now().strftime('%H:%M:%S')
        return f"the current time is {now}"
    if "date" in user_input or "day" in user_input:
        today = datetime.date.today()
        return f"Today is {today.strftime('%A:d%:%B:%Y')}"
    
    for key, reply in intents.items():
        if key in user_input:   # keyword match
            return reply
    return None
