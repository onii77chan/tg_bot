import sqlite3
from DB import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('bot_database.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print('connect to database')

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.commit()
