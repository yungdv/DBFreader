from django.db import models

class EquipmentType(models.Model):
    name = models.CharField(max_length=100)

class Model(models.Model):
    name = models.CharField(max_length=100)
    typeequid = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)

class Hardware(models.Model):
    sn = models.CharField(max_length=100)
    modelid = models.ForeignKey(Model, on_delete=models.CASCADE)