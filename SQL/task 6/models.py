import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'

    publisher_id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    publisher_name = sq.Column(sq.String(60), unique=True)

    def __str__(self):
        return f'(id : {self.id}: name: {self.name})'

    book = relationship('Book', back_populates='publisher')


class Book(Base):
    __tablename__ = 'book'

    book_id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(60), unique=True, nullable=False)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.publisher_id'), nullable=False)

    publisher = relationship(Publisher, backref='book_id')

    def __str__(self):
        return f'(book_id: {self.id}, title: {self.title}, publisher_id: {self.publisher_id})'


class Shop(Base):
    __tablename__ = 'shop'

    shop_id = sq.Column(sq.Integer, primary_key=True)
    shop_name = sq.Column(sq.String(60), unique=True)

    def __str__(self):
        return f'shop_id: {self.id}: shop_name: {self.name}'


class Stock(Base):
    __tablename__ = 'stock'

    stock_id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.book_id'), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.shop_id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    book = relationship(Book, backref='book_stock')
    shop = relationship(Shop, backref='shop_stock')

    def __str__(self):
        return f'(stock_id: {self.stock.id}, book_id: {self.book_id},' \
               f'shop_id: {self.shop_id}, count: {self.count})'


class Sale(Base):
    __tablename__ = 'sale'

    sale_id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.stock_id'), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stock = relationship(Stock, backref='sale_id')

    def __str__(self):
        return f'(sale_id: {self.sale.id}, price: {self.price}, date_sale: {self.date_sale},' \
               f'stock_id: {self.stock_id}, count: {self.count})'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
