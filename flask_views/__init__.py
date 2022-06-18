from flask import Flask

from flask_views.models import db


def create_user():
    app = Flask(__name__)
    app.config.from_object('flask_views.settings.ConfigDebug')
    db.init_app(app)
    return app


app_ctx = create_user()
