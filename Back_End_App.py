import mysql.connector
import pandas as pd
import time

connection = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=''
)

cursor = connection.cursor()


def read_user_information():
    command = "SELECT * FROM users;"
    listagem = pd.read_sql(command, con=connection)
    return listagem


def write_user_information(user_login, user_password):
    command = f"INSERT INTO users (user_login, user_password) VALUES ('{user_login}', '{user_password}')"
    cursor.execute(command)
    connection.commit()

