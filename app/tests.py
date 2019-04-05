from django.test import TestCase
from .models import *

# Create your tests here.

class EmployeeTestClass(TestCase):
    #setUp method
    def setUp(self):
        self.james=Employee(first_name='james',last_name='odipo',Salary='12.00',department='ICT')

    def test_instance(self):
        self.assertTrue(isinstance(self.james,Employee))

    #testing save method
    def test_save_method(self):
        self.james.save_employee()
        employee = Employee.objects.all()
        self.assertTrue(len(employee)>0)


    
