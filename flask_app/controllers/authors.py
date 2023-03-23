from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.authors import Authors
from flask_app.models.books import Books

@app.route('/')
def index():
    return redirect("/authors")

@app.route('/authors')
def authors():
    all_authors = Authors.get_all_authors()
    return render_template("new_author.html", all_authors=all_authors)


@app.route('/authors/create', methods=['POST'])
def create_author():
    author_data = {
        'name':request.form['name']
    }
    Authors.save(author_data)
    return redirect('/authors')
    
@app.route('/authors/<int:id>')
def show_author(id):
    author_name= {
        "id":id
    }
    author = Authors.authors_favorites(author_name)
    unfavorited_books = Books.unfavorited_books(author_name)
    return render_template('authors.html', author = author, unfavorited_books=unfavorited_books)

@app.route('/authors/add/favorite',methods=['POST'])
def add_favorite_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Authors.add_favorite(data)
    return redirect(f"/authors/{request.form['author_id']}")