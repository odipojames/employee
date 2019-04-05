from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.

class Employee(models.Model):
    department=(

            ('ICT','ICT'),
            ('Finance','Finance'),
            ('Admin','Admin'),
    )
    department=models.CharField(max_length=60,choices=department)
    by = models.CharField(max_length=60)
    first_name = models.CharField(max_length = 60, unique=True)
    last_name = models.CharField(max_length = 60)
    Salary = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField(auto_now_add=True)
    # employee_image = models.ImageField(upload_to = 'employees/',blank=True)
    def __str__(self):
        return self.first_name

    def save_employee(self):
        self.save()

    def delete_employee(self):
        self.delete()

    @classmethod
    def get_employee(cls):
        employee=Employee.objects.all()
        return employee


    @classmethod
    def  get_singleEmployee(cls,id):
         singlEmployee = Employee.objects.filter(id=id)
         return singlEmployee

    @classmethod
    def search_by_department(cls,department):
        employee = cls.objects.filter(department__icontains=department)
        return employee
