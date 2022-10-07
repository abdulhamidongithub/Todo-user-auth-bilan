from django.contrib.auth.models import User
from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=50)
    guruh = models.CharField(max_length=50, blank=True)
    st_raqam = models.CharField(max_length=50, blank=True)
    tel = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):return self.fullname

class Plan(models.Model):
    sarlavha = models.CharField(max_length=30)
    batafsil = models.TextField(blank=True)
    status = models.CharField(max_length=12,default="Yangi")
    sana = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.sarlavha


