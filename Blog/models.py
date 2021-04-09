from django.db import models


# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=40)
    reenter_password = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name


# class Login(models.Model):
#     last_name = models.CharField(max_length=30)
#     password = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.last_name


class Blogger(models.Model):
    Blogger_Phone_Number = models.CharField(max_length=20)
    Blogger_Name = models.CharField(max_length=20)
    Blogger_email = models.EmailField()
    Blog_Detail = models.CharField(max_length=500)

    class Meta:
        db_table = "employee"
