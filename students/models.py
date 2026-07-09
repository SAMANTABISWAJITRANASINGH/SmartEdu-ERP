from django.db import models

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    course = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    admission_date = models.DateField(
    null=True,
    blank=True)

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.first_name