from django.shortcuts import render
from .models import Employee
from rest_framework.viewsets import ModelViewSet
from .serializer import EmpSer

class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmpSer

