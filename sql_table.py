import psycopg2
from settings import *
from psycopg2 import Error


try:

    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database='homework_1'
    )
    cursor = connection.cursor()

    # create table-------------
    # create_table_query = '''CREATE TABLE contacts
    # (
    #     id INT PRIMARY KEY NOT NULL,
    #     name TEXT          NOT NULL,
    #     email TEXT         NOT NULL,
    #     password TEXT      NOT NULL
    # );
    # '''
    # cursor.execute(create_table_query)
    # connection.commit()
    # print('Table contacts created!')

    # add 10 users------------
    # insert_query = '''INSERT INTO contacts(id, name, email, password) VALUES
    # (1, 'Bill', 'bill@gmail.com', 'qwe123'),
    # (2, 'Tom', 'tom@mail.ru', 'zxcqwe'),
    # (3, 'Mark', 'mark@yandex.ru', 'qwe123zxcasd'),
    # (4, 'Monica', 'monice@po4ta.com', 'cat123'),
    # (5, 'Brian', 'brian@myea.com', 'my_pas'),
    # (6, 'Floyd', 'floyd@gmail.com', 'money123'),
    # (7, 'Maks', 'maks@gmail.com', 'querosa'),
    # (8, 'Zoe', 'zoe@gmail.com', 'my_qwe_123'),
    # (9, 'Bob', 'bob@gmail.com', 'password1923'),
    # (10, 'Anny', 'anny@gmail.com', 'opasdq')
    # '''
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Add user:', cursor.fetchone)

    # select users who have gmail

    # take_query = """SELECT id,name,email,password FROM contacts WHERE email like '%@gmail.com%'"""
    # cursor.execute(take_query)
    # connection.commit()
    # print('Users with gmail.com :', cursor.fetchall())

    # change password user who have id 4

    # change_query = """UPDATE contacts SET password = 123 WHERE id = 4"""
    # cursor.execute(change_query)
    # connection.commit()
    # print('You changed password!')

    # delete user = Bill

    # delete_query = """DELETE FROM contacts WHERE name = 'Bill' """
    # cursor.execute(delete_query)
    # connection.commit()
    # print('User Bill was deleted')

    # show all users first word = A

    # take_query_name_a = """SELECT id, name, email,password FROM contacts WHERE name like 'A%'"""
    # cursor.execute(take_query_name_a)
    # connection.commit()
    # print('Result for select A:', cursor.fetchall())
except(Exception, Error) as error:
    print('Error connection', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed')
