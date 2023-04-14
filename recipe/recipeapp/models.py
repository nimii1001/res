from django.db import models

class UsersTable(models.Model):
    username = models.CharField(max_length = 20,default="")
    password = models.CharField(max_length = 20,default="")