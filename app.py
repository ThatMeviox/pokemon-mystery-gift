from flask import Flask, request, jsonify

app = Flask(__name__)

# Twoja baza kodów i nagród
# W przyszłości możesz to połączyć z BotGhostem przez API
GIFTS = {
    "RANKED-START": {"item": "Master Ball", "amount": 5, "message": "Nagroda za start sezonu!"},
    "LEGIT-PLAYER": {"item": "Rare Candy", "amount": 10, "message": "Dzieki za gre fair play!"}
}

@app.route('/')
def home():
    return "Serwer Mystery Gift dla Ryujinx działa!"

@app.route('/receive', methods=['POST'])
def receive_gift():
    data = request.get_json()
    user_code = data.get("code")

    if user_code in GIFTS:
        print(f"Kod {user_code} zaakceptowany!")
        return jsonify({
            "status": "success",
            "reward": GIFTS[user_code]
        }), 200
    else:
        return jsonify({"status": "error", "message": "Niepoprawny kod"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
