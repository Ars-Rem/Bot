import sqlite3

try:
    class SQLiter:

        def __init__(self, database_file_db_user):
            self.connection = sqlite3.connect(database_file_db_user)
            self.create_table = '''CREATE TABLE sub (
                                                    id         INTEGER NOT NULL
                                                                       PRIMARY KEY AUTOINCREMENT,
                                                    user_id    INTEGER    NOT NULL,
                                                    first_name TEXT,
                                                    last_name  TEXT,
                                                    phone_number     INTEGER,
                                                    item       TEXT,
                                                    date       INTEGER
                                                );

                                    CREATE TABLE "text"  (
                                                            id      INTEGER NOT NULL
                                                                            PRIMARY KEY AUTOINCREMENT,
                                                            user_id INTEGER    NOT NULL,
                                                            text    TEXT    
                                                            );'''

            self.cursor = self.connection.cursor()
            print("База данных подключена к SQLite")
            try:
                self.cursor.executescript(self.create_table)
                self.connection.commit()
                print("Таблица SQLite создана")

                # self.cursor.close()
            except sqlite3.OperationalError:
                print('База создана')

        '''def add_callback(self, user_id, first_name, text, datetime):
            with self.connection:
                print('ok')
                return self.cursor.execute("INSERT INTO 'sub' ('user_id', 'first_name', 'item', 'date') VALUES (?,?,"
                                           "?,?)",
                                           (user_id, first_name, text, datetime))'''

        def add_callback(self, user_id, first_name, last_name, item, datetime):
            with self.connection:
                print('ok')
                return self.cursor.execute("INSERT INTO 'sub' ('user_id', 'first_name', 'last_name', 'item', 'date')"
                                           " VALUES (?,?,?,?,?)",
                                           (user_id, first_name, last_name, item, datetime))

        def add_text(self, user_id, text):
            with self.connection:
                return self.cursor.execute("INSERT INTO text (user_id, text) VALUES (?,?)", (user_id, text))

        def send_recording(self):
            with self.connection:
                li = [self.cursor.execute("SELECT MAX(id), first_name, item, date FROM 'sub'").fetchall()]
                #  lid = {'name': {li[0][0][1]}, 'items:': {li[0][0][2]}, 'date_time:': {li[0][0][3]}}
                #  li = [db.send_recording()]

                answer = "Ім'я: {},\nНайменування: {},\nНомер телефону:{} ,\nДата/час: {}" \
                    .format(li[0][0][1], li[0][0][2],
                            self.cursor.execute("""SELECT sub.id, db_phone.phone_number 
                                                FROM sub INNER JOIN db_phone ON sub.user_id = db_phone.user_id 
                                                ORDER BY sub.id DESC LIMIT 1""").fetchall(), li[0][0][3])
                return answer
                #  SELECT * FROM TableName WHERE id=(SELECT max(id) FROM TableName);
                #  return self.cursor.execute("SELECT DISTINCT 'first_name' FROM 'sub'").fetchall()
                #  return self.cursor.fetchall()

        def send_callback_all(self):
            with self.connection:
                self.cursor.execute("SELECT max(id), first_name, item, date FROM 'sub'")
                return self.cursor.fetchone()

        def return_all(self):
            with self.connection:
                last0 = self.cursor.execute("""SELECT first_name, item, date FROM sub ORDER BY id DESC LIMIT 4""").fetchall()
                #last1 = self.cursor.execute("""SELECT phone_number FROM db_phone ORDER BY id DESC
                # LIMIT 10""").fetchall()
                cont = self.cursor.execute("""SELECT sub.id, sub.first_name, sub.item, sub.date, db_phone.phone_number 
                    FROM sub INNER JOIN db_phone ON sub.user_id = db_phone.user_id 
                    ORDER BY sub.id DESC LIMIT 5""").fetchall()

                print("Замовлення №:{}:\nІм'я: {}\nЩо: {}\nДата: {}\nТелефон: {}\n  {}"\
                    .format(cont[0][0], cont[0][1], cont[0][2], cont[0][3], cont[0][4], last0))

                return "Замовлення №:{}:\nІм'я: {}\nЩо: {}\nДата: {}\nТелефон: {}"\
                    .format(cont[0][0], cont[0][1], cont[0][2], cont[0][3], cont[0][4])


    class USER:
        def __init__(self, database_file_db_sub):
            self.connection = sqlite3.connect(database_file_db_sub)
            self.create_table = '''CREATE TABLE "db_user" (
                                            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                            "user_id"	INTEGER NOT NULL,
                                            "first_name"	TEXT,
                                            "last_name"	TEXT,
                                            "status"	NUMERIC NOT NULL DEFAULT 'True',
                                            "date"	INTEGER);'''

            self.cursor = self.connection.cursor()
            print("База данных подключена к SQLite")
            try:
                self.cursor.execute(self.create_table)
                self.connection.commit()
                print("Таблица SQLite создана")

                # self.cursor.close()
            except sqlite3.OperationalError:
                print('База создана')

        def get_sudscribtions(self, status=True):
            with self.connection:
                return self.cursor.execute("SELECT * FROM 'db_user' WHERE 'status' = ?", (status,)).fetchall()

        def subscriber_exist(self, user_id):
            with self.connection:
                result = self.cursor.execute("SELECT * FROM 'db_user' WHERE 'user_id' = ?", (user_id,)).fetchall()
                return bool(len(result))

        def add_subscriber(self, user_id, first_name, last_name, datetime, status=True):
            with self.connection:
                return self.cursor.execute("INSERT INTO 'db_user' ('user_id', 'first_name', 'last_name',"
                                           " 'status', 'date') VALUES (?,?,?,?,?)",
                                           (user_id, first_name, last_name, status, datetime))

        def update_subscription(self, user_id, status):
            return self.cursor.execute("UPDATE 'db_user' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))


    class PHONE:
        def __init__(self, database_file_db_phone):
            self.connection = sqlite3.connect(database_file_db_phone)
            self.create_table = '''CREATE TABLE "db_phone" (
                                            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                             "user_id"	INTEGER,
                                            "phone_number"	TEXT NOT NULL);'''

            self.cursor = self.connection.cursor()
            print("База данных подключена к SQLite")
            # if base is create give exeption
            try:
                self.cursor.execute(self.create_table)
                self.connection.commit()
                print("Таблица SQLite создана")

                # self.cursor.close()
            except sqlite3.OperationalError:
                print('База создана')

        def add_phone_number(self, user_id, phone_number):
            with self.connection:
                return self.cursor.execute("INSERT INTO db_phone (user_id, phone_number)"
                                           " VALUES (?,?)", (user_id, phone_number))


    class ALL:
        def __init__(self, database_file_db_all):
            self.connection = sqlite3.connect(database_file_db_all)
            self.create_table = '''CREATE TABLE db_all (
                                                        id           INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        user_id      INTEGER,
                                                        first_name   TEXT,
                                                        last_name    TEXT,
                                                        phone_number TEXT    REFERENCES db_phone (phone_number) ON UPDATE CASCADE,
                                                        item         TEXT,
                                                        text         TEXT,
                                                        date         INTEGER
);'''

            self.cursor = self.connection.cursor()
            print("База данных подключена к SQLite")
            # if base is create give exeption
            try:
                self.cursor.execute(self.create_table)
                self.connection.commit()
                print("Таблица SQLite создана")

                # self.cursor.close()
            except sqlite3.OperationalError:
                print('База создана')

        def merged(self, user_id, first_name, last_name, item, datetime):
            while self.connection:
                return self.cursor.execute("INSERT INTO 'db_all' ('user_id', 'first_name', 'last_name', 'item', 'date')"
                                           " VALUES (?,?,?,?,?)",
                                           (user_id, first_name, last_name, item, datetime))

        def merged1(self):
            while self.connection:
                return self.cursor.execute("""INSERT INTO 'db_all' (user_id, first_name, last_name, date)
         SELECT user_id, first_name, last_name, date FROM sub""").fetchone()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)

finally:
    def close(self):
        self.connection.close()
        print("Соединение с SQLite закрыто")
