#!/usr/bin/env python3
"""
This module creates a Flask app.
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel


class Config:
    """
    This class configures available languages in our app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
babel: Babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """
    This function returns a template.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
