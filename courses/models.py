from django.db import models


class Course(models.Model):

    course_id = models.AutoField(primary_key=True)

    course_name = models.CharField(max_length=100)

    course_code = models.CharField(max_length=20, unique=True)

    department = models.CharField(max_length=100)

    duration = models.CharField(max_length=50)

    fees = models.DecimalField(max_digits=10, decimal_places=2)

    total_seats = models.PositiveIntegerField()

    available_seats = models.PositiveIntegerField()

    coordinator = models.CharField(max_length=100)

    description = models.TextField(blank=True)

    photo = models.ImageField(
        upload_to="courses/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name