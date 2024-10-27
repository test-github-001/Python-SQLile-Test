import sqlite3
from msilib.schema import Error

class DataBase():
    # name - Имя базы данных [строка], ПРИМЕР: DataBase('test') -> 'test.db'
    def __init__(self, name):
        self.connect = sqlite3.connect(f'{name}.db')
        self.cursor = self.connect.cursor()
        print(f'\n\n-- Connect to "{name}" DataBase --\n')

    # name is string;
    # structure is  dictionary[key-> column name; value -> column type]
    # first key is primary
    def create_table (self, name, structure):
        structure_string = ''
        primary = False
        for key in structure:
            if not primary:
                structure_string += f'{key} {structure[key]} PRIMARY KEY AUTOINCREMENT'
                primary = True
            else:
                structure_string += f', {key} {structure[key]}'

        query = f'CREATE TABLE IF NOT EXISTS {name}({structure_string})'
        print('QUERY =', query)
        self.cursor.execute(query)
        self.connect.commit()
    
    # table[string] - table name
    # data[tuple] - data tuple
    def add_table_data(self, table, data):
        print(f'GET TO ADD {table}:', data)
        try:
            values = 'VALUES(NULL'
            for i in range(len(data)) : values += ', ?'
            values += ')'
            self.cursor.execute(f"INSERT INTO {table} {values};", data)
            self.connect.commit()
        except Error:
            print(Error)

    # table[string] - table name
    def show_table(self, table):
        self.cursor.execute(f"SELECT * FROM {table};")
        print(self.cursor.fetchall())

    # table[string] - table name
    # data_id[int] - primary key
    def get_table_data_by_id (self, table, data_id):
        self.cursor.execute(f"SELECT * FROM {table} WHERE id = ?;", (data_id,))
        return self.cursor.fetchone()

    # table[string] - table name
    # data[dictionary] - table_key: new_value 
    def edit_table_data(self, table, data):
        try:
            data_id = 0
            keys = ''
            values = []
            for key in data:
                if key == 'id' : data_id = data[key]
                else:
                    keys += f'{key} = ?, '
                    values.append(data[key])
            keys = keys[0: len(keys) - 2] + ' WHERE id = ?'
            values.append(data_id)
            print('keys:', keys)
            self.cursor.execute(f'UPDATE {table} SET {keys};', values)
            self.connect.commit()
            print('UPDATE DONE')
        except Error:
            print(Error)

    # table[string] - table name
    # data_id[int] - primary key
    def delete_from_table_data_id(self, table, data_id):
        # !!! при удалении записи - ваш код должен удалять все связанные данные из других таблиц
        try:
            self.cursor.execute(f'DELETE FROM {table} WHERE id = ?;', (data_id,) )
            self.connect.commit()
        except Error:
            print(Error)

    # Получить число типов ТО по id вида
    def get_from_table_data_value(self, table, data, value):
        self.cursor.execute(f"SELECT * FROM {table} WHERE {data} = ?;", (value,))
        return self.cursor.fetchall()