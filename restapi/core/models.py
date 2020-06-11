from django.db import models

class User(models.Model):
    name = models.CharField(max_length=60)
    cpf = models.CharField(max_length=11)
    birth = models.DateField(max_length=8)

    def __str__(self):
        return self.name

class Salary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.FloatField()
    discounts = models.FloatField()
    payday = models.DateField()