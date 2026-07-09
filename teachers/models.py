from django.db import models

# Create your models here.


class Teacher(models.Model):

    teacher_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=10)

    dob = models.DateField()

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    qualification = models.CharField(max_length=100)

    department = models.CharField(max_length=100)

    joining_date = models.DateField(null=True, blank=True)

    salary = models.DecimalField(max_digits=10, decimal_places=2)

    photo = models.ImageField(
        upload_to="teachers/",
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"