from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import forms
from django.contrib.auth.models import AbstractUser

class Demand(models.Model):
    title = models.CharField(max_length=50, )
    html_file = models.TextField(default="")
    file = models.ImageField(upload_to="statistics\\images")
    html_excel = models.TextField(default="")
    excel = models.FileField(upload_to="statistics\\excel")

    def __str__(self):
        return self.title


class Geography(models.Model):
    title = models.CharField(max_length=50, )
    html_file = models.TextField(default="")
    file = models.ImageField(upload_to="statistics\\images", default=None)
    html_excel = models.TextField(default="")
    excel = models.FileField(upload_to="statistics\\excel",  default=None)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=50, )
    html_file = models.TextField(default="")
    file = models.ImageField(upload_to="statistics\\images")
    html_excel = models.TextField(default="")
    excel = models.FileField(upload_to="statistics\\excel")
    def __str__(self):
        return self.title


class Home(models.Model):

    title = models.CharField(max_length=50, )
    file = models.ImageField(upload_to="home/images")
    html = models.TextField(default="")

    def __str__(self):
        return self.title
#
#
# class Buyer(AbstractUser):
#     ...


