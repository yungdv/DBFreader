from dbfread import DBF
import pandas as pd
import dbf


def read_dbf_with_dbfread(dbf_file):
    try:
        table = DBF(dbf_file, ignore_missing_memofile=True)
        records = [record for record in table]
        df = pd.DataFrame(records)

        print(df)
    except Exception as e:
        print(f"Ошибка при чтении файла {dbf_file} с помощью dbfread: {e}")

new_dbf_file = 'hwidb/USER.DBF'

read_dbf_with_dbfread(new_dbf_file)