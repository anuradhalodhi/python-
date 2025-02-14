from django.db import models



# Create your models here.
class StudentMarks(models.Model):
    sub1=models.IntegerField()
    sub2=models.IntegerField()
    sub3=models.IntegerField()
    sub4=models.IntegerField()
    sub5=models.IntegerField()

