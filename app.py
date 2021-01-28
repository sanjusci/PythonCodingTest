from flask import Flask
from flask_restful import Api

from routes import register_urls

app = Flask(__name__)

app.url_map.strict_slashes = False

api = Api(
    app,
)

register_urls(api)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
