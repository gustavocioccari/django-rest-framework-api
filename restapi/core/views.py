from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, SalarySerializer
from .models import User, Salary

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer