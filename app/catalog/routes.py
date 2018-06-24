from app.catalog import main
from app import db
from app.catalog.models import Book, Publication
from flask import render_template
# use blueprint to create routes, as we don't have acess to the app on a global level
@main.route('/')

def display_books():
    books=Book.query.all()
    return render_template('home.html',books=books)