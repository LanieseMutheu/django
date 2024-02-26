from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=20, null=False)
    phone = models.IntegerField()
    email = models.EmailField(blank= False)

    def __str__(self):
        return self.name

class teacher(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(blank= False)
    tscnumber = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name
