from flask import Flask, jsonify, request # Dodaj request tutaj

# ... poprzedni kod od /ping ...

@app.route('/login-log', methods=['POST'])
def login_log():
    data = request.json
    username = data.get('user', 'Nieznany')
    print(f"--- TRENER ZALOGOWANY: {username} ---")
    return jsonify({"status": "received"}), 200
