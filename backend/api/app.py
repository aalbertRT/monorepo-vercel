from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.config.from_prefixed_env()

if app.config.get("MODE") == "staging":
    CORS(app)

@app.route("/")
def index():
    return {"message": "Hello Mr Rambo, you're hitting the api"}
