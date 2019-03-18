from django import forms
from django.db import models
class Registration(models.Model):
    email=models.EmailField()
    login=models.CharField(max_length=128)
    password=models.CharField(max_length=128)

    def __str__(self):
        return "Пользователь: %s" % (self.login)

