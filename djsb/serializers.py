from django.db.models import Sum
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from djsb.models import Employee, Department


class DepartmentEmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = 'id', 'first_name', 'last_name', 'middle_name', 'photo', 'position', 'age'


class DepartmentSerializer(ModelSerializer):
    employees_count = SerializerMethodField()
    salary_sum = SerializerMethodField()

    class Meta:
        model = Department
        fields = 'id', 'name', 'head', 'employees_count', 'salary_sum'

    def get_employees_count(self, obj: Department):
        return obj.employees.count()

    def get_salary_sum(self, obj: Department):
        return obj.employees.aggregate(Sum('salary'))['salary__sum']


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = 'id', 'first_name', 'last_name', 'middle_name', 'photo', 'position', 'age', 'department'
