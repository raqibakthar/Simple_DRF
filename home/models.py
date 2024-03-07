from django.db import models

# Create your models here.

class Department(models.Model):
    department = models.CharField(max_length=50)
    tutor = models.CharField(max_length=50)

    def __str__(self):
        return self.department
    
class People(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(Department,on_delete = models.CASCADE,null = True,blank=True)

    def __str__(self):
        return self.name