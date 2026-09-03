from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Hello DevOps!"

    @app.route("/health")
    def health():
        return {"status": "ok"}

    @app.route("/about")
    def about():
        return "DevOps Lab Project"

    return app