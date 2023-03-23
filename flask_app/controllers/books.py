from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.books import Books
from flask_app.models.authors import Authors

@app.route('/books')
def books():
    all_books = Books.get_all_books()
    return render_template('new_books.html', all_books = all_books)

@app.route('/book/create', methods=['POST'])
def create_book():
    book_data = {
        'title':request.form['title'],
        'number_of_pages':request.form['number_of_pages']
    }
    Books.save(book_data)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    book_data = {
        "id":id
    }
    return render_template('books.html',book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))