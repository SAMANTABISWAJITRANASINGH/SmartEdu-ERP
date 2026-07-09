from django.db import models


class Department(models.Model):

    department_id = models.AutoField(primary_key=True)

    department_name = models.CharField(max_length=100)

    department_code = models.CharField(max_length=20, unique=True)

    hod = models.CharField(max_length=100)

    email = models.EmailField(blank=True)

    phone = models.CharField(max_length=15, blank=True)

    location = models.CharField(max_length=100, blank=True)

    total_teachers = models.PositiveIntegerField(default=0)

    total_students = models.PositiveIntegerField(default=0)

    description = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to="departments/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name