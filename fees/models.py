from django.db import models
from students.models import Student


class Fee(models.Model):

    STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("Pending", "Pending"),
        ("Partial", "Partial"),
    )

    PAYMENT_CHOICES = (
        ("Cash", "Cash"),
        ("UPI", "UPI"),
        ("Credit Card", "Credit Card"),
        ("Debit Card", "Debit Card"),
        ("Net Banking", "Net Banking"),
    )

    fee_id = models.AutoField(primary_key=True)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    department = models.CharField(max_length=100)

    course = models.CharField(max_length=100)

    fee_type = models.CharField(max_length=100)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    paid_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_date = models.DateField()

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES
    )

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
        return f"{self.student.first_name} - {self.fee_type}"