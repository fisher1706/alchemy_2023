from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey
from configuration import CONNECTION_ROW

meta = MetaData()

authors = Table("Authors", meta,
                Column('id_author', Integer, primary_key=True),
                Column('name', String(250), nullable=False)
                )

books = Table("Books", meta,
              Column('id_book', Integer, primary_key=True),
              Column('title', String, nullable=False),
              Column('author_id', Integer, ForeignKey('Authors.id_author')),
              Column('genre', String(250)),
              Column('price', Integer)
              )

print(books.c.author_id)
print(books.primary_key)

print(authors.c.name)
print(authors.primary_key)
print(authors.c)

engine = create_engine(CONNECTION_ROW, echo=True)
meta.create_all(engine)

print('*' * 200)

conn = engine.connect()

ins_author_query = authors.insert().values(name='Lutz')
conn.execute(ins_author_query)

print('*' * 200)

ins_book_query = books.insert().values(title='Lean Python', author_id=1, genre='Education', price=1299)
conn.execute(ins_book_query)

print('*' * 200)

ins_book_query_2 = books.insert().values(title='Clear Python', author_id=1, genre='Education', price=956)
conn.execute(ins_book_query_2)

print('*' * 200)

books_gr_1000_query = books.select().where(books.c.price > 1000)
result = conn.execute(books_gr_1000_query)

for row in result:
    print(row)

print('*' * 200)

join = select([books, authors]).where(books.c.author_id == authors.c.id_author)
result = conn.execute(join)

for row in result:
    print(row)
