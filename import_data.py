import os
import django
from dbfread import DBF

# Задайте путь к настройкам Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from inventory.models import Hardware, Model, EquipmentType

# Пути к вашим DBF файлам
hardware_dbf = "dbfiles/HARDWARE.DBF"
model_dbf = "dbfiles/MODELID.DBF"
typeequip_dbf = "dbfiles/TYPEEQUID.DBF"

# Чтение данных из DBF файлов
hardware_table = DBF(hardware_dbf, ignore_missing_memofile=True)
model_table = DBF(model_dbf, ignore_missing_memofile=True)
typeequip_table = DBF(typeequip_dbf, ignore_missing_memofile=True)

# Создание словарей для быстрого поиска моделей и типов оборудования
models_dict = {}
for record in model_table:
    models_dict[record['id']] = record

typeequip_dict = {}
for record in typeequip_table:
    typeequip_dict[record['id']] = record

# Перенос данных из hardware_table в базу данных Django
for record in hardware_table:
    model_record = models_dict.get(record['MODELID'])
    typeequip_record = typeequip_dict.get(model_record['TYPEEQUID'])

    # Создание или получение записи EquipmentType
    equipment_type, created = EquipmentType.objects.get_or_create(
        name=typeequip_record['NAME']
    )

    # Создание или получение записи Model
    model, created = Model.objects.get_or_create(
        name=model_record['NAME'],
        equipment_type=equipment_type
    )

    # Создание записи Hardware
    Hardware.objects.create(
        sn=record['SN'],
        model=model
    )

print("Data imported successfully!")
