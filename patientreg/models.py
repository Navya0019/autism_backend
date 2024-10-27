from django.db import models

# Create your models here.


class Patient(models.Model):
    unique_id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.unique_id} - {self.name}"
