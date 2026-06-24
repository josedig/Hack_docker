import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f"¡Hola desde flask corriendo en Docker!"

@app.route('/app')
def health():
    return {"status": "ok", "app": "flask app"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
