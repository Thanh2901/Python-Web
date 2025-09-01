from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"