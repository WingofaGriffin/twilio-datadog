import os
from flask import Flask, request
from twilio.rest import Client

app = Flask(__name__)

# Find these values at https://twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


@app.route("/", methods=['POST'])
def receive_order():
    message = client.messages.create(
        to=os.environ['PHONE_NUMBER'],
        from_=os.environ['TWILIO_NUMBER'],
        body="Hello, World!")
    return '', 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)