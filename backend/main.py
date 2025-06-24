import http.server
import socketserver
from google import genai
from flask import Flask,jsonify,request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

client = genai.Client(
    api_key = os.getenv("APIKEY")
)

PROMPT = "Can you tell me about this person's Codeforces account in an uplifting and encouraging way? Mention how many problems they've solved, their current and highest rating, contest participation, and any achievements or improvements over time. Make it feel positive and motivating — like you're celebrating their journey in competitive programming. Make it over the top somewhat like glazing. Here is the account : " 

@app.post("/glaze")
def GlazeAccount():
    data = request.get_json()
    print(data)
    handle = data["username"]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = PROMPT + handle
    )

    print(response.text)

    return jsonify(response.text)


@app.route('/')
def home():
    return 'Hello from Flask!'

