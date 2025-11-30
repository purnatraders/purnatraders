
from flask import Flask, request
from kiteconnect import KiteConnect

app = Flask(__name__)

API_KEY = v0aqdumvme8vkbij
API_SECRET = u2cyoo4ismdypixqgtls1atuoiwlr2ua

kite = KiteConnect(api_key=API_KEY)

@app.route("/")
def home():
    login_url = kite.login_url()
    return f"<h3>Click to Login to Zerodha</h3><a href='{login_url}'>Login</a>"

@app.route("/token")
def token():
    req_token = request.args.get("request_token")
    if not req_token:
        return "No request token received."

    try:
        data = kite.generate_session(req_token, API_SECRET)
        access_token = data["access_token"]

        with open("access_token.txt", "w") as f:
            f.write(access_token)

        return f"<h3>Access Token:</h3><p>{access_token}</p>"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
