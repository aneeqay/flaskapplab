from db.run_sql import run_sql
from models.author import Author

def save(author):
    sql = "INSERT INTO authors (name) VALUES (%s) RETURNING *"
    values = [author.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    author.id = id
    return author

def select(id):
    author = None
    sql = "SELECT * FROM authors WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        author = Author(result['name'], result['id'] )
    return author

def delete_all():
    sql = "DELETE FROM authors"
    run_sql(sql)

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'] )
        authors.append(author)
    return authors

def find_author_by_name(name):
    author = None
    sql = "SELECT * FROM authors WHERE name = %s"
    values = [name]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        author = Author(result['name'], result['id'] )
    return author