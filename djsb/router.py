from rest_framework import routers

from djsb.views import EmployeeViewSet, DepartmentViewSet

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewSet)
router.register(r'department', DepartmentViewSet)
