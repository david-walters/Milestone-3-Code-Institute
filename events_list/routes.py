from flask import render_template, redirect, url_for

from events_list import app, db

@app.route('/')
def index():
    return render_template("base.html")