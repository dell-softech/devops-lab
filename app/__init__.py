import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///local.db"
    )

    db.init_app(app)

    @app.route("/")
    def home():
        return "DevOps Task App"

    @app.route("/health")
    def health():
        return {"status": "ok"}

    @app.route("/tasks")
    def tasks():
        items = Task.query.all()

        return {
            "tasks": [
                {"id": item.id, "title": item.title}
                for item in items
            ]
        }

    @app.route("/tasks/create/<title>")
    def create_task(title):
        task = Task(title=title)

        db.session.add(task)
        db.session.commit()

        return {"created": title}

    with app.app_context():
        db.create_all()

    return app