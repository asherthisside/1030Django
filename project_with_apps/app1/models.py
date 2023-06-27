from django.db import models

# Create your models here.
class Employee_manager(models.Model):
    name = models.CharField(max_length=50)
    deptt = models.CharField(max_length=10)
    salary = models.IntegerField()
    doj = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}, Manager of {self.deptt} department"
    
# login -> username | password | time_of_login  