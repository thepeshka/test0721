from django.contrib.admin import ModelAdmin, register

from djsb.models import Employee, Department


@register(Employee)
class EmployeeModelAdmin(ModelAdmin):
    pass


@register(Department)
class DepartmentModelAdmin(ModelAdmin):
    pass
