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
                reference_link TEXT,
                UNIQUE (telegram_id)
                );
                
            CREATE TABLE IF NOT EXISTS ban_users (
                id INTEGER PRIMARY KEY,
                telegram_id INTEGER,
                ban_count INTEGER,
                UNIQUE (telegram_id)
                );
                
            CREATE TABLE IF NOT EXISTS profile (
                id INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER,
                nickname CHAR(50),
                bio TEXT,
                age INTEGER,
                zodiac_sign CHAR(50),
                games TEXT,
                country TEXT,
                photo TEXT,
                UNIQUE (telegram_id)
                );
                
            CREATE TABLE IF NOT EXISTS surveys (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idea TEXT,
                problems TEXT,
                telegram_id INTEGER
            );
            
            CREATE TABLE IF NOT EXISTS admin_raiting (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                admin_telegram_id INTEGER,
                telegram_id INTEGER,
                raiting INTEGER
            );
            CREATE TABLE IF NOT EXISTS like_system (
                id INTEGER PRIMARY KEY,
                owner_telegram_id INTEGER,
                liker_telegram_id INTEGER,
                UNIQUE (owner_telegram_id, liker_telegram_id)
            );
            CREATE TABLE IF NOT EXISTS dislike_system (
                id INTEGER PRIMARY KEY,
                owner_telegram_id INTEGER,
                disliker_telegram_id INTEGER,
                UNIQUE (owner_telegram_id, disliker_telegram_id)
            );
            CREATE TABLE IF NOT EXISTS reference_users (
            id INTEGER PRIMARY KEY,
            owner_telegram_id INTEGER,
            referral_telegram_id INTEGER,
            referral_name TEXT,
            UNIQUE (owner_telegram_id, referral_telegram_id)
            );
            
            CREATE TABLE IF NOT EXISTS wallet (
            id INTEGER PRIMARY KEY,
            telegram_id INTEGER,
            balance INTEGER,
            UNIQUE (telegram_id)
            );            
            ALTER TABLE reference_users ADD COLUMN referral_name TEXT;
            ALTER TABLE users ADD COLUMN reference_link TEXT;
            
            """
            cursor.executescript(query)
            db.commit()

    def kipoha_add_user(self, tg_id, username, first_name, last_name):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO users VALUES (?,?,?,?,?,?)"""
            cursor.execute(query, (None, tg_id, username, first_name, last_name, None))
            db.commit()

    def kipoha_add_profile(self, tg_id, nickname, bio, age, sign, games, country, photo):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO profile VALUES (?,?,?,?,?,?,?,?,?)"""
            cursor.execute(query, (None, tg_id, nickname, bio, age, sign, games, country, photo))
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

    def kipoha_select_profile(self, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'nickname': row[2],
            'bio': row[3],
            'age': row[4],
            'sign': row[5],
            'games': row[6],
            'country': row[7],
            'photo': row[8],
            }
            query = """SELECT * FROM profile WHERE telegram_id = ?"""
            cursor.execute(query, (tg_id,))
            return cursor.fetchone()

    def kipoha_update_profile(self, tg_id, nickname, bio, age, sign, games, country, photo):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """UPDATE profile SET nickname = ?,
                bio = ?,
                age = ?,
                zodiac_sign = ?,
                games = ?,
                country = ?,
                photo = ?
                WHERE telegram_id = ?"""
            cursor.execute(query, (nickname, bio, age, sign, games, country, photo, tg_id))
            db.commit()

    def kipoha_add_survey(self, tg_id, idea, propblem):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO surveys VALUES (?,?,?,?)"""
            cursor.execute(query, (None, idea, propblem, tg_id,))
            db.commit()

    def kipoha_get_survey(self):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """SELECT * FROM surveys"""
            cursor.execute(query)
            return cursor.fetchall()

    def kipoha_select_survey(self, id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """SELECT * FROM surveys WHERE id = ?"""
            cursor.execute(query, (id,))
            return cursor.fetchone()

    def kipoha_add_rate(self, adm_tg_id, tg_id, rate):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO admin_raiting VALUES (?,?,?,?)"""
            cursor.execute(query, (None, adm_tg_id, tg_id, rate))
            db.commit()

    # def kipoha_select_all_profile(self):
    #     with sqlite3.connect(self.name) as db:
    #         cursor = db.cursor()
    #         query = """SELECT * FROM profile"""
    #         cursor.execute(query)
    #         return cursor.fetchall()

    def kipoha_add_like(self, owner, liker):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO like_system VALUES (?,?,?)"""
            cursor.execute(query, (None, owner, liker,))
            db.commit()


    def kipoha_add_dislike(self, owner, disliker):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO dislike_system VALUES (?,?,?)"""
            cursor.execute(query, (None, owner, disliker,))
            db.commit()

    def kipoha_select_all_profiles(self, owner):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            cursor.row_factory = lambda cursor, row: {
                'id': row[0],
                'telegram_id': row[1],
                'nickname': row[2],
                'bio': row[3],
                'age': row[4],
                'sign': row[5],
                'games': row[6],
                'country': row[7],
                'photo': row[8],
            }
            query = """SELECT *
                       FROM profile
                       LEFT JOIN like_system ON profile.telegram_id = like_system.owner_telegram_id AND like_system.liker_telegram_id = ?
                       LEFT JOIN dislike_system ON profile.telegram_id = dislike_system.owner_telegram_id AND dislike_system.disliker_telegram_id = ?
                       WHERE like_system.id IS NULL AND dislike_system.id IS NULL AND profile.telegram_id != ?
                    """
            cursor.execute(query, (owner, owner, owner))
            return cursor.fetchall()

    def kipoha_select_user_referral(self, owner):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            cursor.row_factory = lambda cursor, row: {
                'total_referrals': row[0],
            }
            query = """SELECT
                            COUNT(reference_users.id) as total_referrals
                       FROM
                            users
                       LEFT JOIN
                            reference_users ON users.telegram_id = reference_users.owner_telegram_id
                       WHERE
                            users.telegram_id = ?
                    """
            cursor.execute(query, (owner,))
            return cursor.fetchone()

    def kipoha_select_user(self, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            cursor.row_factory = lambda cursor, row: {
                'id': row[0],
                'telegram_id': row[1],
                'username': row[2],
                'first_name': row[3],
                'last_name': row[4],
                'link': row[5],
            }
            query = """SELECT * FROM users WHERE telegram_id = ?"""
            cursor.execute(query, (tg_id,))
            return cursor.fetchone()

    def kipoha_update_link(self, link, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """UPDATE users SET reference_link = ? WHERE telegram_id = ?"""
            cursor.execute(query, (link, tg_id))
            db.commit()

    def kipoha_select_user_by_link(self, link):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            cursor.row_factory = lambda cursor, row: {
                'id': row[0],
                'telegram_id': row[1],
                'username': row[2],
                'first_name': row[3],
                'last_name': row[4],
                'link': row[5],
            }
            query = """SELECT * FROM users WHERE reference_link = ?"""
            cursor.execute(query, (link,))
            return cursor.fetchone()

    def kipoha_add_referral(self, owner, referral, referral_name):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO reference_users VALUES (?,?,?,?)"""
            cursor.execute(query, (None, owner, referral, referral_name,))
            db.commit()

    def kipoha_get_referral(self, ref_tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """SELECT * FROM reference_users WHERE owner_telegram_id = ?"""
            cursor.execute(query, (ref_tg_id,))
            return cursor.fetchall()

    def kipoha_add_wallet(self, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """INSERT INTO wallet VALUES (?,?,?)"""
            cursor.execute(query, (None, tg_id, 0,))
            db.commit()

    def kipoha_get_wallet(self, tg_id):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            cursor.row_factory = lambda cursor, row: {
                'id': row[0],
                'telegram_id': row[1],
                'balance': row[2],
            }
            query = """SELECT * FROM wallet WHERE telegram_id = ?"""
            cursor.execute(query, (tg_id,))
            return cursor.fetchone()

    def kipoha_update_bal_referral(self, tg_id, money=100):
        with sqlite3.connect(self.name) as db:
            cursor = db.cursor()
            query = """UPDATE wallet SET balance = COALESCE(balance, 0) + ? WHERE telegram_id = ?"""
            cursor.execute(query, (money, tg_id))
            db.commit()