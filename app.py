import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return '<h1><p style="color:' + os.environ.get('APP_COLOR', 'black') + '">g-Bruno-Erick-Daniel-Fred TrabFinal Pratica2 build-app OpenShift Builds repositório git Webhook teste 2</p></h1>'

@app.route('/api')
def hello():
    return '{status: ok}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
