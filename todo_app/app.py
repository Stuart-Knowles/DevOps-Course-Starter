from flask import Flask, render_template, request, redirect

from todo_app.flask_config import Config

from .src import trello_items
from .src.helpers import partition

app = Flask(__name__)
app.config.from_object(Config())


@app.route("/")
def index():
    to_do, done = partition(lambda x: x.status == "Done", trello_items.get_items())
    return render_template("index.html", to_do_items=to_do, done_items=done)


@app.post("/item")
def add_item():
    submitted_title = request.form.get("title")
    if submitted_title is None:
        app.logger.warning("item not provided")
    else:
        trello_items.add_item(submitted_title)
    return redirect("/")


@app.post("/complete_item/<id>")
def complete_item(id):
    trello_items.mark_item_done(id)
    return redirect("/")
