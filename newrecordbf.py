from dbfread import DBF
from dbf import Table, READ_WRITE
import os


def read_dbf_file(dbf_file):
    try:
        table = DBF(dbf_file, ignore_missing_memofile=True)
        for record in table:
            print(record)
    except Exception as e:
        print(f"Ошибка при чтении файла {dbf_file}: {e}")


def add_record_to_dbf(dbf_file, record_data):
    try:

        table = Table(dbf_file, codepage='cp866', ignore_memos=True)
        table.open(READ_WRITE)

        field_names = table.field_names
        filtered_record_data = {key: value for key, value in record_data.items() if key in field_names}

        table.append(filtered_record_data)
        table.close()

        print(f"Запись успешно добавлена в файл {dbf_file}")
    except Exception as e:
        print(f"Ошибка при добавлении записи в файл {dbf_file}: {e}")


def process_directory(directory, record_data):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.dbf'):
            dbf_file = os.path.join(directory, filename)
            print(f"Обработка файла: {dbf_file}")
            read_dbf_file(dbf_file)
            add_record_to_dbf(dbf_file, record_data)


new_record = {
    'field': 'значение',
}

directory_path = ('dbfiles')
process_directory(directory_path, new_record)
