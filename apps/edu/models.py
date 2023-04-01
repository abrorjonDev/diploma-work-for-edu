from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(upload_to='courses', null=True)
    status = models.BooleanField(default=True)
    teacher = models.ForeignKey('edu.Teacher', models.CASCADE)
    price = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    fish = models.CharField("Full name", max_length=100)
    age = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=300)
    level = models.CharField(max_length=100)

    def __str__(self):
        return self.fish
    

class Student(models.Model):
    fish = models.CharField("Full name", max_length=100)
    level = models.CharField(max_length=100)
    contact = models.CharField(max_length=100, default="")
    tag = models.CharField(max_length=300, default="")
    courses = models.ManyToManyField(Course)

    def __str__(self) -> str:
        return self.fish


class FormRequest(models.Model):
    fish = models.CharField("Full name", max_length=120)
    phone = models.CharField("Phone number", max_length=13)
    comment = models.TextField()
    is_seen = models.BooleanField(default=False)

    def __str__(self):
        return self.fish
