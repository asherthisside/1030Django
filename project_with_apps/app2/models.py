from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    deptt = models.CharField(max_length=10)
    salary = models.IntegerField()
    doj = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name + " | " + self.deptt
    
class Student(models.Model):
    name = models.CharField(max_length=35)
    father_name = models.CharField(max_length=35)
    mother_name = models.CharField(max_length=35)
    address = models.TextField()
    dob = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} S/O {self.father_name}"
    
class Guest(models.Model):
    name = models.CharField(max_length=35)
    address = models.CharField(max_length=40)
    doa = models.DateField()

    def __str__(self):
        return self.name + " from " + self.address
    
class Room(models.Model):
    room_no = models.IntegerField()
    guest = models.OneToOneField(Guest, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.room_no)
