import sqlalchemy as sq
import config as c
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Stock, Book, Shop, Sale
from sqlalchemy_utils import database_exists, create_database
import json


name_db = 'book_shop'
DSN = f'postgresql://{c.user}:{c.password}@{c.host}:{c.port}/{name_db}'
engine = sq.create_engine(DSN)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

with open('tests_data.json') as file:
    DATA = json.load(file)


def add_data(data: list, *models):
    for model in models:
        string = str(model).lower()
        model_str = string[25:].strip("'>")
        for dictionary in data:
            if dictionary['model'] == model_str:
                session.add(model(id=dictionary.get('pk'), **dictionary.get('fields')))
            session.commit()


def output_publisher(pers_input):
    if pers_input.isdigit():
        query = session.query(Publisher).filter(Publisher.id == pers_input).all()
    else:
        query = session.query(Publisher).filter(Publisher.name == pers_input).all()
    if query:
        for output in query:
            return output
    return 'Publisher with this id does not exist'


def output_shop(pers_input):
    query = session.query(Shop)
    query = query.join(Stock)
    query = query.join(Book)
    query = query.join(Publisher)
    if pers_input.isdigit():
        query = query.filter(Publisher.id == pers_input).all()
    else:
        query = query.filter(Publisher.name == pers_input).all()
    if query:
        for output in query:
            return output
    return 'Publisher with this id does not exist'


session.close()

if __name__ == "__main__":
    add_data(DATA, Publisher, Book, Shop, Stock, Sale)
    publisher = input(f"Enter publisher ID or Name: ")
    print(publisher)
    print(output_publisher(publisher))
    # print(output_shop(publisher))
