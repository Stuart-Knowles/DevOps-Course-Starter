from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config

from .src import trello
from .src.view import ViewModel

app = Flask(__name__)
app.config.from_object(Config())


@app.route("/")
def index():
    view = ViewModel(items=trello.get_items())
    return render_template("index.html", view=view)


@app.post("/item")
def add_item():
    submitted_title = request.form.get("title")
    if submitted_title is None:
        app.logger.warning("item not provided")
    else:
        items.add_item(submitted_title)
    return redirect("/")


@app.post("/complete_item/<id>")
def complete_item(id):
    items.mark_item_done(id)
    return redirect("/")
