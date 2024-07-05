from dbfread import DBF

def print_dbf_structure(dbf_file):
    try:
        table = DBF(dbf_file, ignore_missing_memofile=True)
        for field in table.fields:
            print(f"Field name: {field.name}, Type: {field.type}, Length: {field.length}")
    except Exception as e:
        print(f"Ошибка при чтении структуры файла {dbf_file}: {e}")

dbf_file = 'dbfiles/TYPEEQU.DBF'
print_dbf_structure(dbf_file)