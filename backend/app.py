from flask import Flask
from flask_cors import CORS

from blueprints.edge import edge

app = Flask(__name__)
app.config.from_prefixed_env()

if app.config.get("MODE") == "staging":
    CORS(app)

app.register_blueprint(edge, url_prefix="/api")
