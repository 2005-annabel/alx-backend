#!/usr/bin/env python3
"""
This module creates a Flask app.
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel, gettext as _
from typing import (
    List,
    Dict,
    Optional
)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user() -> Optional[Dict]:
    """
    """
    id: Optional[int]
    if "login_as" in request.args:
        id = int(request.args.get("login_as"))
    else:
        id = None

    if (id is not None) and (id in users):
        return users[id]
    return None


@app.before_request
def before_request() -> None:
    """
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
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
    home_title: str = _("home_title")
    home_header: str = _("home_header")
    name: Optional[str] = g.user.get("name") if g.user else None
    logged_in_as: str = _("logged_in_as", name=name)
    not_logged_in: str = _("not_logged_in")
    return render_template(
                           "5-index.html",
                           home_title=home_title,
                           home_header=home_header,
                           logged_in_as=logged_in_as,
                           not_logged_in=not_logged_in
                           )


if __name__ == "__main__":
    app.run()
