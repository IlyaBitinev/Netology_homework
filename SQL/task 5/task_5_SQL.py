import psycopg2
import os
from config import db_name, user_name, password


def delete_table(conn, cur, *names_table):
    for name in names_table:
        cur.execute(f"""
                DROP TABLE IF EXISTS {name} CASCADE;
            """)
        conn.commit()
        print(f'Таблица с наименованием - {name}, удалена!')


def create_table(conn, cur):
    cur.execute('''
    CREATE TABLE IF NOT EXISTS clients (
    client_id SERIAL PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL 
    );
    CREATE TABLE IF NOT EXISTS phones (
    client_id INTEGER NOT NULL REFERENCES clients (client_id) ON DELETE CASCADE,
    phone VARCHAR(40) UNIQUE NOT NULL
    );
    ''')
    print('Таблицы с наименованием - clients и phones, созданы!')


def add_client(conn, cur, first_name: str, last_name: str, email: str, phones: tuple = None):
    cur.execute('''
    INSERT INTO clients (first_name, last_name, email)
    VALUES (%s, %s, %s) RETURNING client_id;
    ''', (first_name, last_name, email))
    client_id = cur.fetchone()[0]
    print(f'Добавлен новый клиент - {first_name} {last_name}, присвоен id {client_id}')
    if phones:
        for phone in phones:
            add_phone(conn, cur, client_id, phone)


def add_phone(conn, cur, client_id: int, phone: str):
    cur.execute('''
    INSERT INTO phones (client_id, phone)
    VALUES (%s, %s);
    ''', (client_id, phone))
    print(f'Клиенту с id {client_id} добавлен телефон - {phone}')


def change_client(conn, cursor, name_table, client_id, **values):
    for key, value in values.items():
        cursor.execute(f"""
            UPDATE {name_table}
               SET {key} = {value}
             WHERE client_id = {client_id}
        """)
        conn.commit()
    cursor.execute(f"""
        SELECT * 
          FROM {name_table} 
         WHERE client_id = {client_id}
    """)
    print(f'Данные обновлены - {cursor.fetchone()}')


def del_phone(conn, cur, name_table, client_id, phone):
    cur.execute(f"""
        DELETE FROM {name_table}
         WHERE client_id = {client_id} AND phone = {phone}
    """)
    conn.commit()
    print(f"Номер телефона - {phone} удален у клиента с id - {client_id}")


def del_client(conn, cur, name_table, client_id):
    cur.execute(f"""
        DELETE FROM {name_table}
         WHERE client_id = {client_id}
    """)
    conn.commit()
    print(f"Клиент с id - {client_id} удален из базы данных")


def find_client(cur, **kwargs):
    for key, value in kwargs.items():
        cur.execute(f"""
            SELECT *
              FROM clients 
             INNER JOIN phones USING (client_id)
             WHERE %s = '%s';
        """ % (key, value))
        result = cur.fetchall()
        if result:
            print(f'Клиент найден: {result}')
        else:
            print(f'Клиент не найден!')


if __name__ == '__main__':
    conn = psycopg2.connect(database=db_name, user=user_name, password=password)
    try:
        with conn:
            with conn.cursor() as cur:
                delete_table(conn, cur, 'clients', 'phones')
                create_table(conn, cur)
                add_client(conn, cur, "Ilya", "Bitinev", "bitinev@gmail.com", ("+79108410389", "+79776672132"))
                add_client(conn, cur, "Sofya", "Bitineva", "bta@gmail.com", ("+79018765432",))
                change_client(conn, cur, "clients", 1, email="'bit@gmail.com'")
                del_phone(conn, cur, "phones", 1, "'+79108410389'")
                del_client(conn, cur, "clients", 1)
                find_client(cur, email="bta@gmail.com")
    finally:
        conn.close()
