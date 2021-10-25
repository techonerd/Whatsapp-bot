from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    # getting random quotes from quotable API
    if "quote" in incoming_msg:
        # return a quote
        r = requests.get("https://api.quotable.io/random")
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = "I could not retrieve a quote at this time, sorry."
        msg.body(quote)
        responded = True

    # getting random cat image
    if "cat" in incoming_msg:
        # return a cat pic
        msg.media("https://cataas.com/cat")
        responded = True

    # hinting users about possible methods
    if not responded:
        msg.body("I only know about famous quotes and cats, sorry!")
    return str(resp)


if __name__ == "__main__":
    app.run()
