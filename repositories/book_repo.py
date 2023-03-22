from db.run_sql import run_sql
from models.book import Book

import repositories.author_repo as author_repo

def save(book):
    sql = "INSERT INTO books (title, author_id, link, image_url) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.link, book.image]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = author = author_repo.select(result['author_id'])
        book = Book(result['title'], author, result['link'], result['image_url'], result['id'])
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repo.select(row['author_id'])
        book = Book(row['title'], author, row['link'], row['image_url'], row['id'])
        books.append(book)
    return books

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def find_book_by_title_author(title, author):
    book = None
    author = author_repo.find_author_by_name(author)
    if author:
        sql = "SELECT * FROM books WHERE title = %s AND author_id = %s"
        values = [title, author.id]
        results = run_sql(sql, values)
        if results:
            result = results[0]
            author = author_repo.select(result['author_id'])
            book = Book(result['title'], author, result['link'], result['image_url'], result['id'])
    return book
