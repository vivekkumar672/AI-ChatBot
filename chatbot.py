from flask import Blueprint, request, jsonify
from services.gemini import ask_gemini
from intents.intents import check_intent   # ✅ import intent checker

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    # Step 1: Check intent
    intent_reply = check_intent(user_input)
    if intent_reply:
        return jsonify({"response": intent_reply})

    # Step 2: Fallback to Gemini API
    reply = ask_gemini(user_input)
    return jsonify({"response": reply})

