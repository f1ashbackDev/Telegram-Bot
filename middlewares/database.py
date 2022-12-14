import psycopg2
import config
from psycopg2 import Error

try:
    conn = psycopg2.connect(f"dbname='{config.connectionSetting['database']}'\
        user='{config.connectionSetting['user']}'\
            password='{config.connectionSetting['password']}'")
    print('Connection to Database is good')
    
except Exception as err:
    print(f'Connection to Database is Failed. Error {err}')

async def CreateUser(user, city):
    try:
        cursor = conn.cursor()
        query = f"INSERT INTO users (user_id, city) VALUES ('{user}', '{city}')"
        cursor.execute(query)
        conn.commit()
        print(f'Аккаунт с ид {user} был создан!')
    except (Exception, Error) as error:
        print("Ошибка при работе с SQL", error)

async def getUserData(user):
    try:
        cursor = conn.cursor()
        query = f"select * from users where user_id = {user}"
        cursor.execute(query)
        userCheck = cursor.fetchall()
        if userCheck != None:
            return True
    except (Exception, Error) as error:
        print("Ошибка при работе с SQL", error)

async def getUserCity(user):
    try:
        cursor = conn.cursor()
        query = f"select * from users where user_id = {user}"
        cursor.execute(query)
    except (Exception, Error) as error:
        print('Ошибка при работе с SQL', error)