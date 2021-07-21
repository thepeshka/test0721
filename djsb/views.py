from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from djsb.models import Employee, Department
from djsb.serializers import EmployeeSerializer, DepartmentSerializer


class DepartmentViewSet(ListModelMixin, GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(ListModelMixin, CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['last_name', 'department__id']
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination
    pagination = 20

