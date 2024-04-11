import sqlite3

db_name = 'school.sqlite'


class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def do(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def create(self):
        self.cursor.execute('PRAGMA foreign_key=on')
        self.do('''CREATE TABLE IF NOT EXISTS admins(
                                                id INTEGER PRIMARY KEY,
                                                name VARCHAR,
                                                surname VARCHAR,
                                                middle_name VARCHAR,
                                                username VARCHAR,
                                                password VARCHAR,
                                                unical_code VARCHAR)
                                                ''')
        self.do('''CREATE TABLE IF NOT EXISTS users(
                                                id INTEGER PRIMARY KEY,
                                                class_index VARCHAR,
                                                name VARCHAR,
                                                surname VARCHAR,
                                                middle_name VARCHAR,
                                                username VARCHAR,
                                                password VARCHAR,
                                                unical_code VARCHAR)
                                                    ''')
        self.do('''CREATE TABLE IF NOT EXISTS teachers(
                                                        id INTEGER PRIMARY KEY,
                                                        name VARCHAR,
                                                        surname VARCHAR,
                                                        middle_name VARCHAR,
                                                        username VARCHAR,
                                                        password VARCHAR,
                                                        unical_code VARCHAR,
                                                        isadmin VARCHAR)
                                                        ''')
        self.do('''CREATE TABLE IF NOT EXISTS classroom_teachers(
                                                        id INTEGER PRIMARY KEY,
                                                        name VARCHAR,
                                                        surname VARCHAR,
                                                        middle_name VARCHAR,
                                                        username VARCHAR,
                                                        password VARCHAR,
                                                        unical_code VARCHAR,
                                                        isadmin VARCHAR)
                                                            ''')



        self.do('''CREATE TABLE IF NOT EXISTS groups(
                                                    id INTEGER PRIMARY KEY,
                                                    group_name VARCHAR,
                                                    unical_code VARCHAR)
                                                    ''')
        self.do('''CREATE TABLE IF NOT EXISTS teachers_messages(
                                                                id INTEGER PRIMARY KEY,
                                                                text VARCHAR,
                                                                time VARCHAR,
                                                                unical_code VARCHAR,
                                                                isadmin VARCHAR)
                                                                ''')
        self.do('''CREATE TABLE IF NOT EXISTS classroom_teachers_messages(
                                                                        id INTEGER PRIMARY KEY,
                                                                        text VARCHAR,
                                                                        time VARCHAR,
                                                                        user_login,
                                                                        unical_code VARCHAR,
                                                                        isadmin VARCHAR)
                                                                        ''')

        self.do('''CREATE TABLE IF NOT EXISTS class_10а(
                                                        id INTEGER PRIMARY KEY,
                                                        class_index VARCHAR,
                                                        name VARCHAR,
                                                        surname VARCHAR,
                                                        middle_name VARCHAR,
                                                        username VARCHAR,
                                                        password VARCHAR,
                                                        unical_code VARCHAR
                                                        isadmin)
                                                        ''')
        self.do('''CREATE TABLE IF NOT EXISTS messages_class_10а(
                                                        id INTEGER PRIMARY KEY,
                                                        text_message VARCHAR,
                                                        time_message VARCHAR,
                                                        unical_code VARCHAR,
                                                        isadmin VARCHAR)
                                                        ''')

        self.do('''CREATE TABLE IF NOT EXISTS class_10б(
                                                    id INTEGER PRIMARY KEY,
                                                    class_index VARCHAR,
                                                    name VARCHAR,
                                                    surname VARCHAR,
                                                    middle_name VARCHAR,
                                                    username VARCHAR,
                                                    password VARCHAR,
                                                    unical_code VARCHAR)
                                                    ''')
        self.do('''CREATE TABLE IF NOT EXISTS messages_class_10б(
                                                                id INTEGER PRIMARY KEY,
                                                                text VARCHAR,
                                                                time VARCHAR,
                                                                user_login)
                                                                ''')

        self.do('''CREATE TABLE IF NOT EXISTS class_10в(
                                                    id INTEGER PRIMARY KEY,
                                                    class_index VARCHAR,
                                                    name VARCHAR,
                                                    surname VARCHAR,
                                                    middle_name VARCHAR,
                                                    username VARCHAR,
                                                    password VARCHAR,
                                                    unical_code VARCHAR)
                                                    ''')
        self.do('''CREATE TABLE IF NOT EXISTS messages_class_10в(
                                                                id INTEGER PRIMARY KEY,
                                                                text VARCHAR,
                                                                time VARCHAR,
                                                                user_login)
                                                                ''')

    def create_profiles(self, unical_code):
        self.cursor.execute('PRAGMA foreign_key=on')
        self.do(f'''CREATE TABLE IF NOT EXISTS student_{unical_code}(
                                                        id INTEGER PRIMARY KEY,
                                                        class_index VARCHAR,
                                                        name VARCHAR,
                                                        surname VARCHAR,
                                                        middle_name VARCHAR,
                                                        unical_code VARCHAR,
                                                        status,
                                                        about_user,
                                                        phone_number,
                                                        avatar_photo)
                                                        ''')

    def first_insert_into_users(self, class_index, name, surname, middle_name, username, password, unical_code):
        self.cursor.execute('INSERT into users(class_index, name, surname, middle_name, username, password, unical_code) VALUES(?,?,?,?,?,?,?)', [class_index, name, surname, middle_name, username, password, unical_code])
        self.conn.commit()

    def first_insert_into_admins(self, name, surname, middle_name, username, password, unical_code):
        self.cursor.execute('INSERT into admins(name, surname, middle_name, username, password, unical_code) VALUES(?,?,?,?,?,?)', [name, surname, middle_name, username, password, unical_code])
        self.conn.commit()

    def first_insert_into_teachers(self, name, surname, middle_name, username, password, unical_code, isadmin):
        self.cursor.execute('INSERT into teachers(name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?)', [name, surname, middle_name, username, password, unical_code, isadmin])
        self.conn.commit()

    def first_insert_into_school_news(self, name, surname, middle_name, username, password, unical_code, isadmin):
        self.cursor.execute('INSERT into School_news(name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?)', [name, surname, middle_name, username, password, unical_code, isadmin])
        self.conn.commit()

    def first_insert_into_english_teachers(self, name, surname, middle_name, username, password, unical_code, isadmin):
        self.cursor.execute('INSERT into english_teachers(name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?)', [name, surname, middle_name, username, password, unical_code, isadmin])
        self.conn.commit()

    def first_insert_into_pe_teachers(self, name, surname, middle_name, username, password, unical_code, isadmin):
        self.cursor.execute('INSERT into pe_teachers(name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?)', [name, surname, middle_name, username, password, unical_code, isadmin])
        self.conn.commit()

    def first_insert_into_classroom_teachers(self, name, surname, middle_name, username, password, unical_code, isadmin):
        self.cursor.execute('INSERT into classroom_teachers(name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?)', [name, surname, middle_name, username, password, unical_code, isadmin])
        self.conn.commit()

    def first_insert_into_users_10_a(self, class_index, name, surname, middle_name, username, password, unical_code, value):
        self.cursor.execute('INSERT into class_10а(class_index, name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?,?)', [class_index, name, surname, middle_name, username, password, unical_code, value])
        self.conn.commit()

    def first_insert_into_users_10_b(self, class_index, name, surname, middle_name, username, password, unical_code, value):
        self.cursor.execute('INSERT into class_10б(class_index, name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?,?)', [class_index, name, surname, middle_name, username, password, unical_code, value])
        self.conn.commit()

    def first_insert_into_users_10_v(self, class_index, name, surname, middle_name, username, password, unical_code, value):
        self.cursor.execute('INSERT into class_10в(class_index, name, surname, middle_name, username, password, unical_code, isadmin) VALUES(?,?,?,?,?,?,?,?)', [class_index, name, surname, middle_name, username, password, unical_code, value])
        self.conn.commit()

    def first_insert_into_profiles(self, class_index, name, surname, middle_name, unical_code, status, about_user, phone_number, avatar_photo):
        self.cursor.execute(f'INSERT INTO student_{unical_code}(class_index, name, surname, middle_name, unical_code, status, about_user, phone_number, avatar_photo) VALUES(?,?,?,?,?,?,?,?,?)', [class_index, name, surname, middle_name, unical_code, status, about_user, phone_number, avatar_photo])
        self.conn.commit()

    def first_insert_into_groups(self, group_name, unical_code):
        self.cursor.execute('INSERT INTO groups(group_name, unical_code) VALUES(?,?)', [group_name, unical_code])
        self.conn.commit()

    def delete_from_profiles(self, unical_code):
        self.cursor.execute(f'DROP TABLE IF EXISTS student_{unical_code}')
        self.conn.commit()

    def check_users(self, username):
        self.cursor.execute('SELECT username from users WHERE username=?', [username])
        result = self.cursor.fetchone()
        return result

    def input_user(self, username_input, password_input):
        self.cursor.execute('SELECT username, password FROM users WHERE username=? AND password=?',
                            [username_input, password_input])
        result = self.cursor.fetchone()

        return result

    def input_teacher(self, username_input, password_input):
        self.cursor.execute('SELECT username, password FROM teachers WHERE username=? AND password=?',
                            [username_input, password_input])
        result = self.cursor.fetchone()

        return result

    def input_admin(self, username_input, password_input):
        self.cursor.execute('SELECT username, password FROM admins WHERE username=? AND password=?',
                            [username_input, password_input])
        result = self.cursor.fetchone()
        return result

    def get_name_to_main_window(self, username_global):
        self.cursor.execute('SELECT name, surname, unical_code, class_index FROM users WHERE username=?', [username_global])
        result_name = self.cursor.fetchone()
        return result_name

    def get_name_to_main_window_teacher(self, username_global):
        self.cursor.execute('SELECT name, surname, unical_code FROM teachers WHERE username=?', [username_global])
        result_name = self.cursor.fetchone()
        return result_name

    def get_info_to_admin_pannel(self, username_global):
        self.cursor.execute('SELECT name, surname, unical_code FROM admins WHERE username=?', [username_global])
        result_name = self.cursor.fetchone()
        return result_name

    def delete_student(self, unical_code):
        self.cursor.execute('DELETE from users WHERE unical_code=?', [unical_code])
        self.conn.commit()

    def delete_teacher(self, unical_code):
        self.cursor.execute('DELETE from teachers WHERE unical_code=?', [unical_code])
        self.conn.commit()

    def delete_class(self, unical_code):
        self.cursor.execute('DELETE from groups WHERE unical_code=?', [unical_code])
        self.conn.commit()

    def add_new_class_db(self, name, unical_code):
        self.cursor.execute('INSERT into groups(group_name, unical_code) VALUES(?,?)', [name, unical_code])
        self.conn.commit()

    def check_admin_password(self, password):
        self.cursor.execute('SELECT password from admins WHERE password=?', [password])
        result = self.cursor.fetchone()
        return result

    def get_name_of_class(self, unical_code):
        self.cursor.execute('SELECT group_name from groups WHERE unical_code=?', [unical_code])
        result = self.cursor.fetchone()
        return result

    def get_all_groups_db(self):
        self.cursor.execute('SELECT group_name from groups')
        result = self.cursor.fetchall()
        return result

    def get_users_from_class(self, class_index):
        self.cursor.execute(f'SELECT name, surname, unical_code, isadmin from class_{class_index}')
        result = self.cursor.fetchall()
        return result

    def get_users_from_none_class(self, class_index):
        self.cursor.execute(f'SELECT name, surname, unical_code, isadmin from {class_index}')
        result = self.cursor.fetchall()
        return result

    def check_is_admin(self, unical_code, class_name):
        self.cursor.execute(f'SELECT isadmin from class_{class_name} WHERE unical_code=?', [unical_code])
        result = self.cursor.fetchone()
        return result

    def check_is_admin_none_class(self, unical_code, class_name):
        self.cursor.execute(f'SELECT isadmin from {class_name} WHERE unical_code=?', [unical_code])
        result = self.cursor.fetchone()
        return result

    def send_one_message(self, time_of_message, text_message, unical_code, isadmin, class_index):
        self.cursor.execute(f'INSERT INTO messages_class_{class_index}(text_message, time_message, unical_code, isadmin) VALUES(?,?,?,?)',
                            [text_message, time_of_message, unical_code, isadmin])
        self.conn.commit()

    def send_one_message_none_class(self, time_of_message, text_message, unical_code, isadmin, class_index):
        self.cursor.execute(f'INSERT INTO {class_index}_messages(text_message, time_message, unical_code, isadmin) VALUES(?,?,?,?)',
                            [text_message, time_of_message, unical_code, isadmin])
        self.conn.commit()

    def get_id_of_message(self, time, class_index):
        self.cursor.execute(f'''SELECT id, isadmin from messages_class_{class_index} WHERE time_message=?''', [time])
        id_of_message = self.cursor.fetchone()
        return id_of_message

    def get_id_of_message_none_class(self, time, class_index):
        self.cursor.execute(f'''SELECT id, isadmin from {class_index}_messages WHERE time_message=?''', [time])
        id_of_message = self.cursor.fetchone()
        return id_of_message

    def get_unical_code_of_message(self, class_index, id):
        self.cursor.execute(f'SELECT unical_code FROM messages_class_{class_index} WHERE id=?', [id])
        result = self.cursor.fetchone()
        return result

    def get_unical_code_of_message_none_class(self, class_index, id):
        self.cursor.execute(f'SELECT unical_code FROM {class_index}_messages WHERE id=?', [id])
        result = self.cursor.fetchone()
        return result

    def delete_message(self, id_user, class_index, unical_code):
        self.cursor.execute(f'DELETE from messages_class_{class_index} WHERE id=? AND unical_code=?', [id_user, unical_code])
        self.conn.commit()

    def delete_message_none_class(self, id_user, class_index, unical_code):
        self.cursor.execute(f'DELETE from {class_index}_messages WHERE id=? AND unical_code=?', [id_user, unical_code])
        self.conn.commit()

    def get_info_about_user_db(self, unical_code):
        self.cursor.execute(f'''SELECT class_index, name, surname, middle_name, status, about_user, phone_number, avatar_photo from student_{unical_code}''')
        result = self.cursor.fetchall()
        return result

    def update_profile_db(self, unical_code, status, about_user, phone_number):
        self.cursor.execute(f'''UPDATE student_{unical_code} set status=?, about_user=?, phone_number=?''', [status, about_user, phone_number])
        self.conn.commit()

    def create_table_for_ls(self, my_unical_code, other_unical_code):
        self.cursor.execute('PRAGMA foreign_key=on')
        self.do(f'''CREATE TABLE IF NOT EXISTS ls_{my_unical_code}_{other_unical_code}(
                                                                        id INTEGER PRIMARY KEY,
                                                                        text_message VARCHAR,
                                                                        time_message VARCHAR,
                                                                        unical_code INTEGER,
                                                                        isadmin VARCHAR)''')

    def create_table_chats(self):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS chats(
                                                                id INTEGER PRIMARY KEY,
                                                                chat_index VARCHAR)''')
        self.conn.commit()

    def create_table_for_one_teacher(self, unical_code):
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS teacher_{unical_code}(
                                                                                id INTEGER PRIMARY KEY,
                                                                                groups VARCHAR,
                                                                                unical_code VARCHAR)''')
        self.conn.commit()

    def get_all_teachers_groups(self, unical_code):
        self.cursor.execute(f'SELECT groups from teacher_{unical_code}')
        result = self.cursor.fetchall()
        return result

    def add_new_group_to_teacher(self, unical_code, name):
        self.cursor.execute(f'INSERT into teacher_{unical_code}(groups, unical_code) VALUES(?,?)', [name, unical_code])
        self.conn.commit()





a = DataBase()
a.create()
