from flask import Flask

from blueprints.edge import edge

app = Flask(__name__)

app.register_blueprint(edge, url_prefix="/api")

@app.route("/")
def index():
    return "Hello Mr Kennedy, you're on the home page!"
