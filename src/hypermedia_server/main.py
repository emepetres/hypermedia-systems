from flask import Flask

# # from hypermedia_server.settings import app_settings

# Create the Flask application instance
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"
