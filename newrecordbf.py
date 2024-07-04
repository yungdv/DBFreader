from dbfread import DBF
from dbf import Table, READ_WRITE, delete
import os


def get_dbf_fields(dbf_file):
    try:
        table = DBF(dbf_file, ignore_missing_memofile=True)
        dbf_fields = [(field.name, field.type, field.length) for field in table.fields]
        return dbf_fields
    except Exception as e:
        return None


def read_dbf_file(dbf_file):
    try:
        table = DBF(dbf_file, ignore_missing_memofile=True)
        records = [record for record in table]
        print(records)
    except Exception as e:
        pass


def add_record_to_dbf(dbf_file, record_data):
    try:
        table = Table(dbf_file, codepage='cp866', ignore_memos=True)
        table.open(mode=READ_WRITE)

        for rec in table:
            if all(k in rec for k in record_data):
                delete(table, rec.recno)

        table.append(record_data)
        table.close()

        print(f"Запись успешно добавлена в файл {dbf_file}")
    except Exception as e:
        pass


def process_directory(directory, record_data):
    for filename in os.listdir(directory):
        if filename.lower().endswith('.dbf'):
            dbf_file = os.path.join(directory, filename)
            print(f"Обработка файла: {dbf_file}")

            read_dbf_file(dbf_file)
            add_record_to_dbf(dbf_file, record_data)
            read_dbf_file(dbf_file)


if __name__ == "__main__":
    new_record = {
        'USERID': '201',
        'NAME': 'Novikov D.T.',
    }

    directory_path = 'dbfiles'
    process_directory(directory_path, new_record)
