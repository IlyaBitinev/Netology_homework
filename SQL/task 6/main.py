import config as c
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Shop, Publisher, Book, Stock, Sale
import json

DSN = f'postgresql://{c.user}:{c.password}@{c.host}:{c.port}/{c.name_db}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()
with open('tests_data.json') as f:
    data = json.load(f)
    for item in data:
        if item['model'] == 'publisher':
            publisher = Publisher(publisher_id=item['pk'], publisher_name=item['fields']['name'])
            session.add(publisher)
        elif item['model'] == 'book':
            book = Book(book_id=item['pk'], title=item['fields']['title'],
                        publisher_id=item['fields']['id_publisher'])
            session.add(book)
        elif item['model'] == 'shop':
            shop = Shop(shop_id=item['pk'], shop_name=item['fields']['name'])
            session.add(shop)
        elif item['model'] == 'stock':
            stock = Stock(stock_id=item['pk'], book_id=item['fields']['id_book'],
                          shop_id=item['fields']['id_shop'], count=item['fields']['count'])
            session.add(stock)
        else:
            sale = Sale(sale_id=item['pk'], price=item['fields']['price'], date_sale=item['fields']['date_sale'],
                        stock_id=item['fields']['id_stock'], count=item['fields']['count'])
            session.add(sale)
        session.commit()


    def get_publisher() -> str:
        choice = input('Пожалуйста, введите id или имя автора: ')
        shop = []
        if choice.isdigit():
            for item in session.query(Shop).join(Stock, Shop.shop_id == Stock.shop_id). \
                    join(Book, Stock.book_id == Book.book_id).join(Publisher,
                                                                   Book.publisher_id == Publisher.publisher_id). \
                    filter(Publisher.publisher_id == int(choice)).all():
                shop.append(item.shop_name)
            if shop:
                return f'автор опубликовал свои книги в магазине: {", ".join(str(i) for i in shop)}'
            return f'Автор с id - {choice} не найден в базе данных'
        else:
            for item in session.query(Shop).join(Stock, Shop.shop_id == Stock.shop_id). \
                    join(Book, Stock.book_id == Book.book_id).join(Publisher,
                                                                   Book.publisher_id == Publisher.publisher_id). \
                    filter(Publisher.publisher_name == choice).all():
                shop.append(item.shop_name)
            if shop:
                return f'автор опубликовал свои книги в магазине: {", ".join(str(i) for i in shop)}'
            return f'Автор - {choice} не найден в базе данных'

print(get_publisher())
session.close()
