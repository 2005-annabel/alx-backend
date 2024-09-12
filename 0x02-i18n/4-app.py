#!/usr/bin/env python3
"""
This module creates a Flask app.
"""
from flask import (
    Flask,
    render_template,
    request
)
from flask_babel import Babel, _
from typing import (
    List,
    Optional
)


class Config:
    """
    This class configures available languages in our app.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = "en"
    BABEL_DEFAULT_TIMEZONE: str = "UTC"


app: Flask = Flask(__name__)
babel: Babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    This function determines the best match with
    our supported languages.
    """
    local: Optional[str] = request.args.get("locale")
    if (local) and (local in app.config["LANGUAGES"]):
        return local
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """
    This function returns a template.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
