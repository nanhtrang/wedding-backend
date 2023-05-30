from django.db import models


# Create your models here.
class Wish(models.Model):
    name = models.CharField(default="", null=True, blank=True, max_length=200)
    wish = models.TextField()

    def __str__(self):
        return self.name + " - " + self.wish


class Confirm(models.Model):
    name = models.CharField(default="", null=True, blank=True, max_length=200)
    number = models.IntegerField(null=True, default=0)
    isGroomSide = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " - đi " + str(self.number) + " người"


class Account(models.Model):
    username = models.CharField(default="", null=True, blank=True, max_length=50)
    password = models.CharField(default="", null=True, blank=True, max_length=50)
