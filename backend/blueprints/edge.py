from flask import Blueprint
edge = Blueprint("edge", __name__)

@edge.route("")
def index():
    return "Hello Mr Kennedy, you're hitting the api"
