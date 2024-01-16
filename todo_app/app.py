from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config

from .data import session_items

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = session_items.get_items()
    return render_template("index.html", items=items)

@app.post('/item')
def add_item():
    submitted_title = request.form.get('title')
    if submitted_title is None:
        app.logger.warning("item not provided")
    else:
        session_items.add_item(request.form.get('title'))
    return redirect("/")
