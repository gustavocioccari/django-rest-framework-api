from .models import User, Salary
from rest_framework import serializers
from django.db.models import Avg, Max, Min

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = '__all__'

class SalaryDataSerializer(serializers.ModelSerializer):
    avg_salary = serializers.SerializerMethodField()
    avg_discounts = serializers.SerializerMethodField()
    max_salary = serializers.SerializerMethodField()
    min_salary = serializers.SerializerMethodField()

    class Meta:
        model = Salary
        fields = ['avg_salary', 'max_salary', 'min_salary', 'avg_discounts']

    def get_avg_salary(self,obj):
        avgsalary = Salary.objects.filter(user_id=obj.user).values_list('pk',flat=True).aggregate(avg_salary=Avg('salary'))
        return avgsalary['avg_salary']
    def get_avg_discounts(self,obj):
        avgdiscounts = Salary.objects.filter(user_id=obj.user).aggregate(avg_discounts=Avg('discounts'))
        return avgdiscounts['avg_discounts']

    def get_max_salary(self,obj):
        maxsalary = Salary.objects.filter(user_id=obj.user).aggregate(max_salary=Max('salary'))
        return maxsalary['max_salary']

    def get_min_salary(self,obj):
        minsalary = Salary.objects.filter(user_id=obj.user).aggregate(min_salary=Min('salary'))
        return minsalary['min_salary']