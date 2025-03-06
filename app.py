from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7965333508:AAEsZxHzosAoNBa8DSSKcVudfoY2-67effM"
CHAT_ID = "1298432616"

@app.route('/sendMessage', methods=['GET'])
def send_message():
    message = request.args.get('message', 'Fall Detected')
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    params = {
        "chat_id": CHAT_ID,
        "text": message
    }
    response = requests.get(url, params=params)
    return response.text, response.status_code

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
