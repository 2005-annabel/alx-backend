#!/usr/bin/env python3
"""
This module creates a Flask app.
"""
from flask import (
    Flask,
    render_template
)


app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    This function returns a template.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
