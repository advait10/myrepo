import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demoproj.settings')
import django
django.setup()

from testapp.models import Employee
from faker import Faker
from random import randint
fake =Faker()


def populate(n):
    for i in range(1,n+1):
        j = i
        fname = fake.name()
        faddr = fake.address()
        fsal = fake.random.randint(5000,30000)
        emp = Employee.objects.get_or_create(name=fname,addr=faddr,sal=fsal)
        j=i+1
    print('employee added succesfully')

populate(20)