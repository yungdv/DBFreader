from dbfread import DBF

dbf_file = "hwidb/HARDWARE.DBF"

table = DBF(dbf_file, ignore_missing_memofile=True)

for record in table:
    print(record)
