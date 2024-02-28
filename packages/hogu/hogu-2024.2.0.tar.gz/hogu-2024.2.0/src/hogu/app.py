from flask import Flask


try:
    from importlib.metadata import metadata

    __version__ = metadata("hogu")["Version"]
except ImportError:
    __version__ = "2024.0.0"


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"Hogu {__version__}"

    return app
