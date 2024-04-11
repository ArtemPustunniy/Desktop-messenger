import time
from flask import Flask, request, Response
import create_db

app = Flask(__name__)

database = create_db.DataBase()

username_global_user = ''
username_global_admin = ''
username_global_teacher = ''

messages = []

# messages = {'class_10а': [],
#             'class_10б': [],
#             'class_10в': [],
#             'teachers': [],
#             'classroom_teachers': []
#             }


# def get_all_messages():
#     all = database.send_all_messages()
#     for elem in all:
#         message = {'name': elem[0], 'text': elem[2], 'time': float(elem[1])}
#         messages.append(message)
#     print(messages)

def filter_by_key(elements, key, thresold):
    filtered_elements = []
    for elem in elements:
        if elem[key] > thresold:
            filtered_elements.append(elem)
    return filtered_elements


@app.route("/")
def hello():
    return "Working... <a href='/status'>Статус</a>"


@app.route('/enter_user', methods=['POST', 'GET'])
def enter_user():
    global username_global_user
    if request.method == 'POST':
        login = request.json['username']
        username_global_user = request.json['username']
        password = request.json['password']
        full_enter = {'username': login, 'password': password}
        if full_enter['username'] == '' or full_enter['password'] == '':
            return Response(status=400)
        else:
            res = database.input_user(login, password)
            print(res)
            if not res:
                return Response(status=401)
            else:
                if res[0] == login and res[1] == password:
                    return Response(status=200)
    if request.method == 'GET':
        print(username_global_user)
        result = database.get_name_to_main_window(username_global_user)
        print(result)
        return {'name': result[0], 'surname': result[1], 'unical_code': result[2], 'class_index': result[3], 'login': username_global_user}


@app.route('/enter_admin', methods=['POST', 'GET'])
def enter_admin():
    global username_global_admin
    if request.method == 'POST':
        login = request.json['username']
        username_global_admin = request.json['username']
        password = request.json['password']
        full_enter = {'username': login, 'password': password}
        if full_enter['username'] == '' or full_enter['password'] == '':
            return Response(status=400)
        else:
            res = database.input_admin(login, password)
            print(res)
            if not res:
                return Response(status=401)
            else:
                if res[0] == login and res[1] == password:
                    return Response(status=200)
    if request.method == 'GET':
        print(username_global_admin)
        result = database.get_info_to_admin_pannel(username_global_admin)
        print(result)
        return {'name': result[0], 'surname': result[1], 'unical_code': result[2], 'login': username_global_admin}


@app.route('/enter_teacher', methods=['POST', 'GET'])
def enter_teacher():
    global username_global_teacher
    if request.method == 'POST':
        login = request.json['username']
        username_global_teacher = request.json['username']
        password = request.json['password']
        full_enter = {'username': login, 'password': password}
        if full_enter['username'] == '' or full_enter['password'] == '':
            return Response(status=400)
        else:
            res = database.input_teacher(login, password)
            print(res)
            if not res:
                return Response(status=401)
            else:
                if res[0] == login and res[1] == password:
                    return Response(status=200)
    if request.method == 'GET':
        print(username_global_teacher)
        result = database.get_name_to_main_window_teacher(username_global_teacher)
        print(result)
        return {'name': result[0], 'surname': result[1], 'unical_code': result[2], 'login': username_global_teacher}


@app.route('/delete_student', methods=['POST', 'GET'])
def delete_student():
    if request.method == 'POST':
        unical_code_student = request.json['unical_code_student']
        password_admin = request.json['admin_password']
        if database.check_admin_password(password_admin):
            database.delete_student(unical_code_student)
            return Response(status=200)
        else:
            return Response(status=400)


@app.route('/delete_class', methods=['POST', 'GET'])
def delete_class():
    if request.method == 'POST':
        unical_code_student = request.json['unical_code_student']
        password_admin = request.json['admin_password']
        if database.check_admin_password(password_admin):
            database.delete_class(unical_code_student)
            return Response(status=200)
        else:
            return Response(status=400)


@app.route('/delete_teacher', methods=['POST', 'GET'])
def delete_teacher():
    if request.method == 'POST':
        unical_code_student = request.json['unical_code_student']
        password_admin = request.json['admin_password']
        if database.check_admin_password(password_admin):
            database.delete_student(unical_code_student)
            return Response(status=200)
        else:
            return Response(status=400)


@app.route('/add_student', methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        class_index = request.json['class_index']
        name = request.json['name']
        surname = request.json['surname']
        middle_name = request.json['middle_name']
        username = request.json['username']
        password = request.json['password']
        unical_code = str(class_index[3]) + str(name[0]) + str(surname[0]) + str(middle_name[0])
        database.first_insert_into_users(class_index, name, surname, middle_name, username, password, unical_code)
        return Response(status=200)


@app.route('/add_teacher', methods=['POST', 'GET'])
def add_teacher():
    if request.method == 'POST':
        name = request.json['name']
        surname = request.json['surname']
        middle_name = request.json['middle_name']
        username = request.json['username']
        password = request.json['password']
        unical_code = str(password[0]) + str(password[1]) + str(password[2]) + str(password[-1]) + str(password[-2])
        database.first_insert_into_teachers(name, surname, middle_name, username, password, unical_code)
        return Response(status=200)


@app.route('/add_class', methods=['POST', 'GET'])
def add_class():
    if request.method == 'POST':
        letter = request.json['letter']
        index = request.json['index']
        unical_code = request.json['unical_code']
        name = letter + ' ' + index
        database.add_new_class_db(name, unical_code)
        return Response(status=200)


@app.route('/connect_group_by_admin', methods=['POST', 'GET'])
def connect_group_by_admin():
    if request.method == 'GET':
        other_unical_code = request.args['other_unical_code']
        result = database.get_name_of_class(other_unical_code)
        return {'name_of_class': result[0]}
    else:
        password = request.json['password']
        if database.check_admin_password(password):
            return Response(status=200)
        else:
            return


@app.route('/get_all_groups', methods=['POST', 'GET'])
def get_all_groups():
    if request.method == 'GET':
        result = database.get_all_groups_db()
        print(result)
        return {'result': result}


@app.route('/get_all_groups_teachers', methods=['POST', 'GET'])
def get_all_groups_teacher():
    if request.method == 'GET':
        unical_code = request.args['unical_code']
        result = database.get_all_teachers_groups(unical_code)
        print(result)
        return {'result': result}


@app.route('/show_students', methods=['POST', 'GET'])
def show_students():
    if request.method == 'GET':
        class_index = request.args['class_index']
        if str(class_index[0]) in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            result = database.get_users_from_class(class_index)
            return {'result': result}
        else:
            result = database.get_users_from_none_class(class_index)
            return {"result": result}


@app.route("/send", methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        # Запрос данных в json формате из messenger.py
        name = request.json['name']
        text = request.json['text']
        unical_code = request.json['unical_code']
        class_name = request.json['class_index']
        message = {'name': name, 'text': text, 'time': time.time(), 'unical_code': unical_code, 'class_name': class_name}
        message['name'] = message['name'].strip()
        message['text'] = message['text'].strip()
        message['text'] = message['text'].replace('\n', '')
        # Обработка принятых данных
        if message['name'] == '':
            return Response(status=400)
        else:
            if message['text'] == '':
                return Response(status=400)
            else:
                print(message)
                print(message['unical_code'])
                if str(class_name[0]) in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
                    if database.check_is_admin(message['unical_code'], message['class_name'])[0] == 'True':
                        # В общий список словарей messages записывается сообщение
                        database.send_one_message(str(message['time']), message['text'], message['unical_code'], 'True', message['class_name'])
                        messages.append(message)
                        print(messages)
                        return Response(status=200)
                    else:
                        database.send_one_message(str(message['time']), message['text'], message['unical_code'], 'False', message['class_name'])
                        messages.append(message)
                        print(messages)
                        return Response(status=200)
                else:
                    if database.check_is_admin_none_class(message['unical_code'], message['class_name'])[0] == 'True':
                        # В общий список словарей messages записывается сообщение
                        database.send_one_message_none_class(str(message['time']), message['text'], message['unical_code'], 'True', message['class_name'])
                        messages.append(message)
                        print(messages)
                        return Response(status=200)
                    else:
                        database.send_one_message_none_class(str(message['time']), message['text'], message['unical_code'], 'False', message['class_name'])
                        messages.append(message)
                        print(messages)
                        return Response(status=200)
    else:
        if str(request.args['class_name'][0]) in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            some_id = database.get_id_of_message(request.args['time'], request.args['class_name'])
            print(some_id)
            if some_id:
                return {'id': some_id[0], 'isadmin': some_id[1]}
            else:
                return {'id': None}
        else:
            some_id = database.get_id_of_message_none_class(request.args['time'], request.args['class_name'])
            print(some_id)
            if some_id:
                return {'id': some_id[0], 'isadmin': some_id[1]}
            else:
                return {'id': None}


@app.route("/messages")
def messages_view():
    # Параметр after нужен для правильной сортировки сообщений
    after = float(request.args['after'])
    filtered_messages = filter_by_key(messages, 'time', after)
    # Возвращает данные в виде словаря, чтобы можно было использовать json
    return {'messages': filtered_messages}


@app.route("/delmessage", methods=['POST'])
def del_messages():
    unical_code = request.json['my_unical_code']
    id_of_user = request.json['id']
    print('-')
    print(id_of_user)
    print('-')
    class_name = request.json['class_name']
    # print(f'{unical_code} --- {database.get_unical_code_of_message(class_name, id_of_user)}')
    if str(class_name[0]) in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        if unical_code == database.get_unical_code_of_message(class_name, id_of_user)[0]:
            if id_of_user:
                database.delete_message(id_of_user, class_name, unical_code)
                return Response(status=200)
        else:
            return Response(status=201)
    else:
        if unical_code == database.get_unical_code_of_message_none_class(class_name, id_of_user)[0]:
            if id_of_user:
                database.delete_message_none_class(id_of_user, class_name, unical_code)
                return Response(status=200)
        else:
            return Response(status=201)


@app.route('/get_info_about_user')
def get_info_about_user():
    unical_code = request.args['unical_code']
    result = database.get_info_about_user_db(unical_code)
    print(result)
    return {'other_class_index': result[0][0], 'name': result[0][1], 'surname': result[0][2], 'middle_name': result[0][3], 'status': result[0][4], 'about_user': result[0][5], 'phone_number': result[0][6], 'avatar_photo': result[0][7]}


@app.route('/update_profile_user', methods=['POST'])
def update_profile_user():
    unical_code = request.json['unical_code']
    status = request.json['status']
    about_user = request.json['info_about']
    phone_number = request.json['phone_number']
    database.update_profile_db(unical_code, status, about_user, phone_number)
    return Response(status=200)


app.run()
