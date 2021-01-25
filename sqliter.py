import sqlite3

try:
    class SQLiter:

        def __init__(self, database_file_db_user):
            self.connection = sqlite3.connect(database_file_db_user)
            self.create_table = '''CREATE TABLE "sub" (
                                                        "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                                        "user_id"	TEXT NOT NULL,
                                                        "first_name"	TEXT,
                                                        "status"	NUMERIC NOT NULL DEFAULT 'True',
                                                        "number"	INTEGER,
                                                        "item"	TEXT,
                                                        "text"	TEXT,
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

        def add_callback(self, user_id, first_name, text, datetime):
            with self.connection:
                print('ok')
                return self.cursor.execute("INSERT INTO 'sub' ('user_id', 'first_name', 'item', 'date') VALUES (?,?,"
                                           "?,?)",
                                           (user_id, first_name, text, datetime))

        def add_text(self, user_id, text):
            with self.connection:
                return self.cursor.execute("INSERT INTO sub (user_id, text) VALUES (?,?)", (user_id, text))

        def send_recording(self):
            with self.connection:
                li = [self.cursor.execute("SELECT MAX(id), first_name, item, date FROM 'sub'").fetchall()]
                #lid = {'name': {li[0][0][1]}, 'items:': {li[0][0][2]}, 'date_time:': {li[0][0][3]}}
                #  li = [db.send_recording()]
                answer = "Ім'я: {},\nНайменування: {},\nНомер телефону: ,\nДата/час: {}" \
                    .format(li[0][0][1], li[0][0][2], li[0][0][3])
                return answer
                #  SELECT * FROM TableName WHERE id=(SELECT max(id) FROM TableName);
                # return self.cursor.execute("SELECT DISTINCT 'first_name' FROM 'sub'").fetchall()
                # return self.cursor.fetchall()

        def send_callback_all(self):
            with self.connection:
                self.cursor.execute("SELECT max(id), first_name, item, date FROM 'sub'")
                return self.cursor.fetchone()


    class USER:
        def __init__(self, database_file_db_sub):
            self.connection = sqlite3.connect(database_file_db_sub)
            self.create_table = '''CREATE TABLE "db_user" (
                                            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                            "user_id"	TEXT NOT NULL,
                                            "first_name"	TEXT,
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

        def add_subscriber(self, user_id, first_name, datetime, status=True):
            with self.connection:
                return self.cursor.execute("INSERT INTO 'db_user' ('user_id', 'first_name', 'status', 'date') VALUES "
                                           "(?,?,?,?)",
                                           (user_id, first_name, status, datetime))

        def update_subscription(self, user_id, status):
            return self.cursor.execute("UPDATE 'db_user' SET 'status' = ? WHERE 'user_id' = ?", (status, user_id))


    class PHONE:
        def __init__(self, database_file_db_phone):
            self.connection = sqlite3.connect(database_file_db_phone)
            self.create_table = '''CREATE TABLE "db_phone" (
                                            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                            "phone_number"	TEXT NOT NULL,
                                            "first_name"	TEXT,
                                            "last_name"	TEXT,
                                            "user_id"	INTEGER);'''

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

        def add_phone_number(self, number, first_name, last_name, user_id):
            with self.connection:
                return self.cursor.execute("INSERT INTO db_phone (phone_number, first_name, last_name, user_id)"
                                           " VALUES (?,?,?,?)", (number, first_name, last_name, user_id))


    class ALL:
        def __init__(self, database_file_db_all):
            self.connection = sqlite3.connect(database_file_db_all)
            self.create_table = '''CREATE TABLE "db_all" (
                                            "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                            "user_id" INTEGER INT REFERENCES "db_phone",
                                            "first_name" TEXT,
                                            "last_name"	TEXT,
                                            "phone_number" TEXT NOT NULL,
                                            "item"	TEXT,
                                            "text"	TEXT,
                                            "date"	INTEGER);'''

            self.cursor = self.connection.cursor()
            print("База данных подключена к SQLite")
            # if base is create give exeption
            try:
                self.cursor.executescript(self.create_table)
                self.connection.commit()
                print("Таблица SQLite создана")

                # self.cursor.close()
            except sqlite3.OperationalError:
                print('База создана')

        def merged(self):
            while self.connection:
                #self.cursor.executescript('''SELECT a.id, a.user_id, a.phone_number, b.id
               # FROM db_phone a INNER JOIN db_all b ON a.id=b.id''')
                return self.cursor.executescript('''SELECT a.phone_number, a.first_name, a.last_name, a.user_id FROM db_phone a INNER JOIN
                                                     db_all b ON a.id = b.id;''')




except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)

finally:
    def close(self):
        self.connection.close()
        print("Соединение с SQLite закрыто")

'''@property
def url(self) -> str:
    """
    Get URL for the message

    :return: str
    """
    if ChatType.is_private(self.chat):
        raise TypeError("Invalid chat type!")
    url = "https://t.me/"
    if self.chat.username:
        # Generates public link
        url += f"{self.chat.username}/"
    else:
        # Generates private link available for chat members
        url += f"c/{self.chat.shifted_id}/"
    url += f"{self.message_id}"

    return url
'''
