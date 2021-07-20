from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        # quote = 'I love you baby <3 <3'
        msg.body(quote)
        responded = True
        
    if 'slaps' in incoming_msg:
        url = "https://markmscott-slapbot-v1.p.rapidapi.com/Twister"

        headers = {
            'x-rapidapi-key': "c5a8b25371mshfb8a44effa986d1p1a4abdjsn1541d6075333",
            'x-rapidapi-host': "markmscott-slapbot-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'norris' or 'chunk' in incoming_msg:
        r = requests.get('https://api.chucknorris.io/jokes/random')
        if r.status_code ==200:
            data = r.json()
            quote = data["value"]
        else:
            quote = 'Ma bad. Got shot, bullet is in critical condition.'
        # quote = 'I love you baby <3 <3'
        msg.body(quote)
        responded = True

    if not responded:
        msg.body('I only know about famous quotes, cats and chunk or norris or norris chunk')
    return str(resp)


if __name__ == '__main__':
    app.run()
