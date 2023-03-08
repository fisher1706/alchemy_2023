from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from configuration import CONNECTION_ROW


engine = create_engine(CONNECTION_ROW, echo=True)
Base = declarative_base()


class Book(Base):
    __tablename__ = 'Books'

    id_book = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey("Authors.id_author"))
    genre = Column(String(250))
    price = Column(Integer, nullable=False)
    author = relationship("Author", backref='zapel')


class Author(Base):
    __tablename__ = 'Authors'

    id_author = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    book = relationship("Book")


Base.metadata.create_all(engine)

print(Book.author)
b = Book()
print(b.author)

a = Author()
print(a.zapel)  # backref = 'zapel' - необходим для этого
