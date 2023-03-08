from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

from configuration import CONNECTION_ROW

engine = create_engine(CONNECTION_ROW, echo=True)
meta = MetaData(engine)

authors = Table('Authors', meta, autoload=True)
books = Table('Books', meta, autoload=True)


class Book:
    def __init__(self, title, author_id, genre, price):
        self.title = title
        self.author_id = author_id
        self.genre = genre
        self.price = price

    def __repr__(self):
        return f"<Book({self.title}, {str(self.author_id)}, {self.genre}, {str(self.price)})>"


class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Author({self.name})>"


mapper(Book, books)
mapper(Author, authors)

new_book = Book("NewBook", 1, "NewG", 2500)

DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(new_book)
session.commit()

for row in session.query(Book).filter(Book.price > 1000):
    print(row)

print('*' * 200)

for row in session.query(Book, Author).filter(Book.author_id == Author.id_author).filter(Book.price > 1000):
    print(f"{row.Book.title}, {row.Author.name}")

print('*' * 200)

second_book = session.query(Book).filter_by(id_book=3).one()
if not isinstance(second_book, list):
    second_book.price = 3000
    session.add(second_book)
    session.commit()

print('*' * 200)

second_book = session.query(Book).filter_by(id_book=2).one()
if second_book:
    print(second_book)

print('*' * 200)

second_book = session.query(Book).filter_by(id_book=2).one()
if second_book:
    print(second_book)
    session.delete(second_book)
    session.commit()

print('*' * 200)

try:
    query_res = session.query(Book).filter_by(id_book=2).one()
except Exception as e:
    print(e)
else:
    print(query_res.price)
