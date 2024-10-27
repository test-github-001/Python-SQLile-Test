from db import DataBase

import datetime
# datetime.date(YYYY, M, D) # (2025, 1, 31)
# datetime.date.today() # (2026, 12, 31)

DB = DataBase('test')

'''
NULL — значение NULL
INTEGER — целое число
REAL — число с плавающей точкой
TEXT — текст
BLOB — бинарное представление крупных объектов, хранящееся в точности с тем, как его ввели
DATE - YYYY-MM-DD
TIME - HH:MM:SS
'''

TABLE_USERS = {
    'id': 'INTEGER',
    'name': 'TEXT',
    'wins': 'INTEGER',
    'registration_date': 'DATE'
}

TABLE_GAMES = {
    'id': 'INTEGER',
    'info': 'TEXT',
}

TABLE_CONNECTIONS_USERS_GAMES = {
    'id': 'INTEGER',
    'game_id': 'INTEGER',
    'user_id': 'INTEGER',
}

DB_TABLES = {
    'users': TABLE_USERS,
    'games': TABLE_GAMES,
    'connections_users_games': TABLE_CONNECTIONS_USERS_GAMES
}

DB.create_table ('users', DB_TABLES['users'])
DB.create_table ('games', DB_TABLES['games'])
DB.create_table ('connections_users_games', DB_TABLES['connections_users_games'])


##################################
#
#  Data Base
#

# test db fill
users_list = [
    # name wins registration_date
    ('Иван', 1, datetime.date(2022, 6, 26)),
    ('Олег', 4, datetime.date(2023, 5, 25)),
    ('Анна', 2, datetime.date(2023, 4, 24)),
    ('Дима', 1, datetime.date(2024, 3, 23)),
    ('Инга', 0, datetime.date(2024, 2, 22)),
    ('Макс', 3, datetime.date(2024, 1, 21)),
]

games_list = [
    # info
    ('Тестовая игра',),
    ('Чемпионат региона',),
    ('Чемпионат мира',)
]

connections_users_games_list = [
    # game_id user_id
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 1),
    (3, 2),
    (3, 3),
    (3, 4),
    (3, 5),
    (3, 6),
]

DB_NAME = 'test'
DB = DataBase(DB_NAME)

for list_item in users_list:
    DB.add_table_data('users', list_item)

for list_item in games_list:
    DB.add_table_data('games', list_item)

for list_item in connections_users_games_list:
    DB.add_table_data('connections_users_games', list_item)

print('-- fill tables with test data READY --')

DB.show_table('users')
DB.show_table('games')
DB.show_table('connections_users_games')

print('-- 2 --')
DB.get_table_data_by_id('users', 2)
DB.edit_table_data('users', {'id': 2, 'name': 'ОЛЕГ', 'wins': 55, 'registration_date': datetime.date(2027, 5, 25)})
DB.get_from_table_data_value('connections_users_games', 'user_id', 2)
print('-- 3 --')
DB.show_table('users')

DB.connect.close()