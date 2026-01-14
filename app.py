from flask import Flask, jsonify

app = Flask(__name__)

# To jest główna strona - opcjonalna
@app.route('/')
def home():
    return "Serwer PokéNet Działa!"

# TO JEST TO, CZEGO SZUKA TWOJA APKA (kod 404 zamieni się w 200)
@app.route('/ping')
def ping():
    return "pong", 200

if __name__ == '__main__':
    # Render wymaga, żeby serwer słuchał na porcie podanym w systemie
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
