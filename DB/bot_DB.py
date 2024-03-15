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

    def sql_insert_user(self, tg_id, user_name, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, user_name, first_name, last_name)
        )
        self.connection.commit()
