import create_db
database = create_db.DataBase()
# database.create_table_chats()
# with open('teachers_logins.csv', 'r', encoding='utf-8') as infile:
#     for line in infile:
#         line = line.strip()
#         b = line.split(';')
#         if b[0] == '':
#             break
#         else:
#             unical_code = str(ord(b[4][0])) + str(ord(b[4][-1])) + str(ord(b[4][-2])) + str(ord(b[4][2]))
#             print(unical_code)
            # database.first_insert_into_school_news(b[0], b[1], '', b[2], b[4], unical_code, 'False')
            # database.create_table_for_one_teacher(unical_code)
# database.first_insert_into_school_news('Артём', 'Пустынный', 'Сергеевич', 'artem', 'qwerty', '1234567890123456', 'True')
# database.first_insert_into_teachers('Артём', 'Пустынный', 'Сергеевич', 'artem', 'qwerty', '1234567890123456', 'True')
# database.first_insert_into_groups('School_news', '999')
# database.first_insert_into_users_10_a('10а', 'Юлия', 'Сундеева', 'Сергеевна', 'yu.sundeeva@school547.ru', 'yu.sundeeva725', '121535046', 'True')
# database.first_insert_into_users_10_v('10в', 'Татьяна', 'Мартынова', 'Александровна', 't.martynova@school547.ru', 't.martynova679', '1165755109', 'True')

# database.first_insert_into_groups('pe_teachers', '243')
# database.first_insert_into_classroom_teachers('Татьяна', 'Мартынова', '', 't.martynova@school547.ru', 't.martynova679', '1165755109', 'False')
# database.first_insert_into_classroom_teachers('Юлия', 'Сундеева', '', 'yu.sundeeva@school547.ru', 'yu.sundeeva725', '121535046', 'False')
# database.first_insert_into_classroom_teachers('Артём', 'Пустынный', 'Сергеевич', 'artem', 'qwerty', '1234567890123456', 'True')
#
# database.first_insert_into_english_teachers('Юлия', 'Сундеева', '', 'yu.sundeeva@school547.ru', 'yu.sundeeva725', '121535046', 'False')
# database.first_insert_into_english_teachers('Марианна', 'Зарубина', '', 'm.zarubina@school547.ru', 'm.zarubina531', '1094951122', 'False')
# database.first_insert_into_english_teachers('Влада', 'Рифтина', '', 'v.riftina@school547.ru', 'v.riftina342', '1185052114', 'False')
# database.first_insert_into_english_teachers('Артём', 'Пустынный', 'Сергеевич', 'artem', 'qwerty', '1234567890123456', 'True')
#
# database.first_insert_into_pe_teachers('Вадим', 'Воинов', '', 'v.voinov@school547.ru', 'v.voinov713', '1185149118', 'False')
# database.first_insert_into_pe_teachers('Вадим', 'Лебедев', '', 'v.lebedev@school547.ru', 'v.lebedev213', '1185149108', 'False')
# database.first_insert_into_pe_teachers('Юлия', 'Удалова', '', 'yu.udalova@school547.ru', 'yu.udalova892', '121505746', 'False')
# database.first_insert_into_pe_teachers('Артём', 'Пустынный', 'Сергеевич', 'artem', 'qwerty', '1234567890123456', 'True')
#
# database.add_new_group_to_teacher('1165755109', '10в')
# database.add_new_group_to_teacher('1165755109', 'classroom_teachers')
# database.add_new_group_to_teacher('1165755109', 'teachers')
# database.add_new_group_to_teacher('1165755109', 'School_news')
#
# database.add_new_group_to_teacher('121535046', '10а')
# database.add_new_group_to_teacher('121535046', 'classroom_teachers')
# database.add_new_group_to_teacher('121535046', 'english_teachers')
# database.add_new_group_to_teacher('121535046', 'teachers')
# database.add_new_group_to_teacher('121535046', 'School_news')
# database.add_new_group_to_teacher('1094951122', 'english_teachers')
# database.add_new_group_to_teacher('1094951122', 'teachers')
# database.add_new_group_to_teacher('1094951122', 'School_news')
# database.add_new_group_to_teacher('1185052114', 'english_teachers')
# database.add_new_group_to_teacher('1185052114', 'teachers')
# database.add_new_group_to_teacher('1185052114', 'School_news')
# database.add_new_group_to_teacher('1185149118', 'teachers')
# database.add_new_group_to_teacher('1185149118', 'pe_teachers')
# database.add_new_group_to_teacher('1185149118', 'School_news')
# database.add_new_group_to_teacher('1185149108', 'teachers')
# database.add_new_group_to_teacher('1185149108', 'pe_teachers')
# database.add_new_group_to_teacher('1185149108', 'School_news')
# database.add_new_group_to_teacher('121505746', 'teachers')
# database.add_new_group_to_teacher('121505746', 'pe_teachers')
# database.add_new_group_to_teacher('121505746', 'School_news')




print(1 // 12)
# with open('logins.csv', 'r', encoding='utf-8') as infile:
#     a = infile.readline()
#     print(a)
#     for line in infile:
#         line = line.strip()
#         b = line.split(';')
#         if b[0] == '':
#             continue
#         else:
#             unical_id = str(ord(b[1][3])) + str(ord(b[2][0])) + str(ord(b[3][0])) + str(ord(b[4][0]))
#             print(b)
#             database.first_insert_into_school_news(b[2], b[3], b[4], b[5], b[6], unical_id, 'False')
#             status = ''
#             about_user = ''
#             phone_number = ''
#             avatar_photo = ''
#             # database.delete_from_profiles(unical_id)
#             # database.create_profiles(unical_id)
#             database.first_insert_into_profiles(b[1], b[2], b[3], b[4], unical_id, status, about_user, phone_number, avatar_photo)
            # database.first_insert_into_profiles(b[1], b[2], b[3], unical_id, None, None, None, None)
# database.first_insert_into_teachers('Юлия', 'Сундеева', 'Сергеевна', 'yuly', 'qwerty1', '0987654321098765')
# database.create_table_for_one_teacher('0987654321098765')
print(ord('.'))
# name = 'Артём'
# surname = 'Пустынный'
# middle_name = 'Сергеевич'
# username = 'artem'
# password = 'qwerty'
# unical_id = '1234567890123456'
#
# database.first_insert_into_admins(name, surname, middle_name, username, password, unical_id)
# database.add_new_group_to_teacher('0987654321098765', '10а')

# class_name = '10a'
#
# a = class_name[-1]
# lst = list(class_name)
# print(lst)
# lst.pop()
# # lst = lst.pop()
# print(lst)
# new = ''.join(lst)
# print(new)
# new_str = new + ' ' + a
# print(new_str)

