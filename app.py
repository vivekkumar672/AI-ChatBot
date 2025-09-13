from flask import Flask, render_template
from flask_cors import CORS
from routes.chatbot import chatbot_bp

app = Flask(__name__)
CORS(app)

# Register routes
# ---------------- DETECT INTENT ----------------


app.register_blueprint(chatbot_bp, url_prefix="/api")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
