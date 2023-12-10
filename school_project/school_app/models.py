from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    c_password = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Department(models.Model):
    dep_name = models.CharField(max_length=200, unique=True)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.dep_name

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.course_name
