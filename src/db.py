import pymysql
import os


def Connect(address: str, port: str, username: str, password: str, db_name: str):
    try:
        connection = pymysql.connect(host=address, port=int(port), user=username, password=password, database=db_name)
        return connection
    except:
        return None
