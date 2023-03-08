from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alchemy_decl import Book, Author
from configuration import CONNECTION_ROW

engine = create_engine(CONNECTION_ROW, echo=True)
session = sessionmaker(bind=engine)
s = session()


author_one = Author(name='Lutz')
s.add(author_one)
s.commit()

author_one = Author(name='Not Lutz')
s.add(author_one)
s.commit()

book_one = Book(title='Cleat Python', author_id=1, genre='Education', price=1500)
s.add(book_one)
s.commit()

s.add_all([
    Book(title='Cleat Python', author_id=1, genre='Education', price=500),
    Book(title='Not Cleat Python', author_id=2, genre='Education', price=2500),
    Book(title='Python as  Python', author_id=1, genre='Education', price=2976),
])
s.commit()

print(s.query(Book).first().title)

for title, price in s.query(Book.title, Book.price).order_by(Book.title).limit(2):
    print(price, title)
