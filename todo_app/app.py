from flask import Flask, render_template

from todo_app.flask_config import Config

from .data import session_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template("index.html", items=items)
