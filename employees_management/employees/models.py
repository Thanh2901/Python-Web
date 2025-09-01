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
    
class WorkSchedule(models.Model):
    class Shift(models.TextChoices):
        MORNING = "morning", "morning"
        AFTERNOON = "afternoon", "afternoon"
        FULL_DAY = "full_day", "full_day"

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="schedules")
    work_day = models.DateField()
    shift = models.CharField(max_length=20, choices=Shift.choices)

    class Meta:
        unique_together = ("employee", "work_day")
        ordering = ["-work_day", "employee_id"]

    def __str__(self):
        return f"{self.employee.email} - {self.work_day} - {self.shift}"