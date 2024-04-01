import sqlite3
from DB import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def sql_create_tables(self):
        try:
            self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
            self.connection.execute(sql_queries.CREATE_BAN_USER_TABLE_QUERY)
            self.connection.execute(sql_queries.CREATE_MANGA_NEWS_TABLE_QUERY)
            self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
            self.connection.commit()
            print("Tables created successfully")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_profile(self, tg_id, nickname, bio, age, married, gender, favorite_color, nationality, photo):
        try:
            self.cursor.execute(
                sql_queries.INSERT_PROFILE_QUERY,
                (None, tg_id, nickname, bio, age, married, gender, favorite_color, nationality, photo)
            )
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error inserting profile: {e}")

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name)
        )
        self.connection.commit()

    def select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def insert_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_BAN_USER_QUERY,
            (None, tg_id, 1)
        )
        self.connection.commit()

    def update_ban_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_COUNT_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def add_manga_news(self, titles):
        self.cursor.execute(sql_queries.INSERT_MANGA_NEWS_QUERY, (None, titles))
        self.connection.commit()

    def reputation_check(self, tg_id):
        self.cursor.execute(
            sql_queries.REPUTATION_CHECK_QUERY,
            (tg_id,)
        )
        result = self.cursor.fetchone()
        self.connection.commit()
        return result[0] if result else "Поздравляю у вас нету нарушений"
