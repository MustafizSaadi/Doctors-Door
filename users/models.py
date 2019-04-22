from django.db import models
from django.contrib.auth.models import User
import datetime
class Person(models.Model):
    gender_choices = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    # email = models.EmailField()
    gender = models.CharField(max_length=20,choices=gender_choices)
    registration_number = models.CharField(max_length=70,default='2016-814-413')
    hall_name = models.CharField(max_length=100,default='Dr. muhammad sahidullah hall')
    department_name = models.CharField(max_length=100)
    admission_year = models.PositiveIntegerField(default=1980)
    phone_number = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)
    date_of_birth = models.DateField(default=datetime.date.today)
    # password = models.CharField(max_length=100)
    # confirm_password = models.CharField(max_length=100)

def _str_(self):
    return self.user.username