from django.db.models import *


class Department(Model):
    name = CharField(max_length=150)
    head = ForeignKey('Employee', on_delete=SET_NULL, null=True, blank=True, related_name='headed_department')

    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Department %s>" % self.__str__()


class Employee(Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100, db_index=True)
    middle_name = CharField(max_length=100)
    photo = ImageField(blank=True, null=True)
    position = CharField(max_length=100)
    salary = PositiveIntegerField()
    age = PositiveIntegerField()
    department = ForeignKey(Department, on_delete=SET_NULL, null=True, blank=True, related_name='employees')

    def __str__(self):
        return "%s %s %s" % (self.last_name, self.first_name, self.middle_name)

    def __repr__(self):
        return "<Employee %s>" % self.__str__()
