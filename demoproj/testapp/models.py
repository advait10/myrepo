from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=50)
    sal = models.FloatField()

    def __str__(self):
        return f'{self.__dict__}'

