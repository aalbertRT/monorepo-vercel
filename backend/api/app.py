from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)
app.config.from_prefixed_env()

if app.config.get("MODE") == "staging":
    CORS(app)

bp = Blueprint("bp", __name__)

@bp.route("/")
def index():
    return {"message": "Hello Mr Rambox, you're hitting the api"}

app.register_blueprint(bp, url_prefix="/api")