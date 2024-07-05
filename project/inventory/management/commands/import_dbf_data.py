from django.core.management.base import BaseCommand
from dbfread import DBF
from inventory.models import TypeEquipment, Model, Hardware
import datetime

class Command(BaseCommand):
    help = 'Import data from DBF files'

    def handle(self, *args, **kwargs):
        self.import_type_equipment()
        self.import_models()
        self.import_hardware()

    def import_type_equipment(self):
        type_equipment_file = 'hwidb/TypeEquID.DBF'
        table = DBF(type_equipment_file, ignore_missing_memofile=True)
        for record in table:
            TypeEquipment.objects.get_or_create(
                typeequid=record['TYPEEQUID'],
                name=record['NAME']
            )

    def import_models(self):
        models_file = 'hwidb/Models.DBF'
        table = DBF(models_file, ignore_missing_memofile=True)
        for record in table:
            type_equipment = TypeEquipment.objects.get(typeequid=record['TYPEEQUID'])
            Model.objects.get_or_create(
                modelid=record['MODELID'],
                name=record['NAME'],
                type_equipment=type_equipment
            )

    def import_hardware(self):
        hardware_file = 'hwidb/Hardware.DBF'
        table = DBF(hardware_file, ignore_missing_memofile=True)
        for record in table:
            model = Model.objects.get(modelid=record['MODELID'])
            created_date = datetime.datetime.strptime(record['CREATED'], '%Y-%m-%d').date()
            Hardware.objects.get_or_create(
                hwid=record['HWID'],
                serial_number=record['SN'],
                inventory_number=record['INVENTN'],
                model=model,
                created_date=created_date
            )