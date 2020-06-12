from django.shortcuts import render
from django.db.models import Avg, Count, Max
from rest_framework import viewsets
from .serializers import UserSerializer, SalarySerializer, SalaryDataSerializer
from .models import User, Salary

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SalaryViewSet(viewsets.ModelViewSet):
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

class SalaryDataViewSet(viewsets.ModelViewSet):
    serializer_class = SalaryDataSerializer
    def get_queryset(self, *args, **kwargs):
        return Salary.objects.filter(user_id=self.request.GET.get('user_pk'))
    
