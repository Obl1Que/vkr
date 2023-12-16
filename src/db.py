import pymysql
import os


class Connection:
    def __init__(self, address: str, port: str, username: str, password: str, db_name: str):
        self.address = address
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name

        self.con = self.Connect()

    def Connect(self):
        try:
            connection = pymysql.connect(host=self.address,
                                         port=int(self.port),
                                         user=self.username,
                                         password=self.password,
                                         database=self.db_name)
            return connection
        except:
            return None
