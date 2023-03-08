from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.sql import select, and_
from configuration import CONNECTION_ROW


engine = create_engine(CONNECTION_ROW, echo=True)
meta = MetaData(engine)

authors = Table('Authors', meta, autoload=True)
books = Table('Books', meta, autoload=True)

conn = engine.connect()

s = select([books, authors]).where(and_(books.c.author_id == authors.c.id_author, books.c.price > 1200))
result = conn.execute(s)

for row in result.fetchall():
    print(row)

delete_query = books.delete().where(books.c.id_book == 1)
conn.execute(delete_query)

update_query = books.update().where(books.c.id_book == '3').values(title='AnotherTitle')
conn.execute(update_query)




