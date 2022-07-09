from django.db import models
# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name