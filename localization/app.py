#!/usr/bin/env python3
"""
babel for translation example
"""

from flask import Flask, request
from flask_babel import Babel, _, ngettext

app = Flask(__name__)
babel = Babel(app)

# Configure default locale and translations directory
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

@babel.localeselector
def get_locale():
    # Select locale from user request Accept-Language headers
    return request.accept_languages.best_match(['en', 'fr'])

@app.route('/')
def index():
    greeting = _("Hello, World!")

    num = 3  # Example number

    # Choose message based on num
    message = ngettext(
        "You have one message",
        "You have %(num)d messages",
        num
    ) % {'num': num}

    # Another example (tacos), done separately
    taco_message = ngettext(
        "You have one taco",
        "You have %(num)d tacos",
        num
    ) % {'num': num}

    return f"{greeting} {message} — {taco_message}"

if __name__ == "__main__":
    app.run(debug=True)
