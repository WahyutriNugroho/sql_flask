# db.py
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                   unix_socket=unix_socket, db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_datas():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM dt;')
        data = cursor.fetchall()
        if result > 0:
            got_datas = jsonify(data)
        else:
            got_datas = 'No Image in DB'
    conn.close()
    return got_datas


def add_data(data):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO dt (name, gender, address, age) VALUES(%s, %s, %s, %s)',
                       (data["name"], data["gender"], data["address"], data["age"]))
    conn.commit()
    conn.close()
