from django.db import models
from students.models import Student


class Examination(models.Model):

    RESULT_CHOICES = (
        ("Pass", "Pass"),
        ("Fail", "Fail"),
    )

    GRADE_CHOICES = (
        ("A+", "A+"),
        ("A", "A"),
        ("B+", "B+"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F"),
    )

    exam_id = models.AutoField(primary_key=True)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    department = models.CharField(max_length=100)

    course = models.CharField(max_length=100)

    subject = models.CharField(max_length=100)

    exam_date = models.DateField()

    total_marks = models.IntegerField()

    obtained_marks = models.IntegerField()

    grade = models.CharField(
        max_length=5,
        choices=GRADE_CHOICES
    )

    result = models.CharField(
        max_length=10,
        choices=RESULT_CHOICES
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.first_name} - {self.subject}"