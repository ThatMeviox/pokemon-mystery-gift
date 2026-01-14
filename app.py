from flask import Flask, jsonify, request

# 1. NAJPIERW tworzymy obiekt aplikacji
app = Flask(__name__)

# 2. POTEM definiujemy trasy (routes)
@app.route('/')
def home():
    return "Serwer PokéNet Działa!"

@app.route('/ping', methods=['GET'])
def ping():
    return "pong", 200

# Nowa trasa do odbierania logów z Twojej aplikacji C#
@app.route('/login-log', methods=['POST'])
def login_log():
    try:
        data = request.json
        username = data.get('user', 'Nieznany')
        print(f"--- TRENER ZALOGOWANY: {username} ---")
        return jsonify({"status": "received", "message": f"Witaj {username}!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# 3. NA KOŃCU uruchamiamy serwer
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
