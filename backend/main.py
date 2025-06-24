import http.server
import socketserver
from google import genai
from flask import Flask,jsonify,request
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

client = genai.Client(
    api_key = os.getenv("APIKEY")
)

PROMPT = "Can you tell me about this person's Codeforces account in an uplifting and encouraging way? Mention how many problems they've solved, their current and highest rating, contest participation, and any achievements or improvements over time. Make it feel positive and motivating — like you're celebrating their journey in competitive programming. Make it over the top somewhat like glazing. Also the blog is going to shown on an html page so please do the formatting accoudinly. Of course please do not add all the tags and such here, but stuff like '\\n' and bold ** will not be shown.Here is the account data : " 


@app.post("/glaze")
def GlazeAccount():
    data = request.get_json()
    print(data)
    handle = data["username"]


    cf_user_api = "https://codeforces.com/api/user.info?handles=" + handle + "&checkHistoricHandles=false"
    print(cf_user_api)

    user_data = requests.get(cf_user_api)
    user_data_res = user_data.text
    print(type(user_data_res))
    print(user_data_res)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents = PROMPT + user_data_res
    )

    print(response.text)

    # return jsonify(handle)
    return jsonify(response.text)


@app.route('/')
def home():
    return 'Hello from Flask!'

