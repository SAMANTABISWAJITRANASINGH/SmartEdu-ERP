from django.db import models
from students.models import Student


class Attendance(models.Model):

    STATUS_CHOICES = (
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Leave", "Leave"),
    )

    attendance_id = models.AutoField(primary_key=True)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    department = models.CharField(max_length=100)

    course = models.CharField(max_length=100)

    attendance_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.student.first_name} - {self.attendance_date}"