import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(60), unique=True)

    def __str__(self):
        return f'(id : {self.id}: name: {self.name})'


class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(60), unique=True, nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='book_id')

    def __str__(self):
        return f'(id: {self.id}, title: {self.title}, id_publisher: {self.publisher_id})'


class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(60), unique=True)

    def __str__(self):
        return f'id: {self.id}: name: {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref='book_stock')
    shop = relationship(Shop, backref='shop_stock')

    def __str__(self):
        return f'(id: {self.id}, book_id: {self.book_id},' \
               f'shop_id: {self.shop_id}, count: {self.count})'


class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='sale_id')

    def __str__(self):
        return f'(id: {self.id}, price: {self.price}, date_sale: {self.date_sale},' \
               f'stock_id: {self.stock_id}, count: {self.count})'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
