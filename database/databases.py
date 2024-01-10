import sqlite3

class DataBase:
    def __init__(self):
        self.name = 'db/data.db'

    def kipoha_create_table(self):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER,
                username CHAR(50),
                first_name CHAR(50),
                last_name CHAR(50),
                UNIQUE (telegram_id)
                )
            """
            cursor.execute(query)
            db.commit()

    def kipoha_add_user(self, tg_id, username, first_name, last_name):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO users VALUES (?,?,?,?,?)"""
            cursor.execute(query, (None, tg_id, username, first_name, last_name))
            db.commit()
