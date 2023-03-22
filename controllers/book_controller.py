from flask import Flask, render_template, Blueprint, request, redirect
from repositories import book_repo
from repositories import author_repo
from models.author import Author
from models.book import Book


books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/books")
def books():
    books = book_repo.select_all()
    return render_template("books/index.html", all_books = books)

@books_blueprint.route('/books/<id>')
def show_books(id):
    book = book_repo.select(id)
    return render_template('books/show.html', book=book)

@books_blueprint.route('/books/<id>/delete', methods = ['POST'])
def delete_book(id):
    book_repo.delete(id)
    return redirect ('/books')

@books_blueprint.route('/books/new')
def new_book():
    return render_template('books/new.html')

@books_blueprint.route('/books', methods = ['POST'])
def add_book():
    title = request.form['title']
    author_name = request.form['author']
    link = request.form['link']
    image = request.form['image']
    if author_repo.find_author_by_name(author_name) == None:
        new_author = Author(author_name)
        author = author_repo.save(new_author)
    else:
        author = author_repo.find_author_by_name(author_name)
    if book_repo.find_book_by_title_author(title, author_name) == None:
        new_book = Book(title, author, link, image)
        book_repo.save(new_book)
    return redirect ('/books')

@books_blueprint.route('/books/<id>/edit')
def edit_book(id):
    book = book_repo.select(id)
    return render_template('books/edit.html', book = book)

# @books_blueprint.route('/books/<id>', methods = ["POST"])
# def update_book(id):
#     pass


