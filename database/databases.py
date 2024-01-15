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
                );
                
            CREATE TABLE IF NOT EXISTS ban_users (
                id INTEGER PRIMARY KEY,
                telegram_id INTEGER,
                ban_count INTEGER,
                UNIQUE (telegram_id)
                )
            """
            cursor.executescript(query)
            db.commit()

    def kipoha_add_user(self, tg_id, username, first_name, last_name):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO users VALUES (?,?,?,?,?)"""
            cursor.execute(query, (None, tg_id, username, first_name, last_name))
            db.commit()

    def kipoha_add_ban_user(self, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO ban_users VALUES (?,?,?)"""
            cursor.execute(query, (None, tg_id, 1,))
            db.commit()

    def kipoha_select_ban_user(self, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            cursor.row_factory = lambda cur, row: {
                'id': row[0],
                'telegram_id': row[1],
                'count': row[2]
            }
            query = """SELECT * FROM ban_users WHERE telegram_id = ?"""
            cursor.execute(query, (tg_id,))
            return cursor.fetchone()

    def kipoha_update_ban_count(self, tg_id):
         with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = 'UPDATE ban_users SET ban_count = ban_count + 1 WHERE telegram_id = ?'
            cursor.execute(query, (tg_id,))
            db.commit()

    def kipoha_check_ban_user(self, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """SELECT * FROM ban_users WHERE telegram_id = ?"""
            cursor.execute(query, (tg_id,))
            return cursor.fetchone()
