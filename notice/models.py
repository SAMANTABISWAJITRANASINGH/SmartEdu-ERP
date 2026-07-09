from django.db import models


class Notice(models.Model):

    STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
    )

    CATEGORY_CHOICES = (
        ("General", "General"),
        ("Examination", "Examination"),
        ("Holiday", "Holiday"),
        ("Placement", "Placement"),
        ("Event", "Event"),
        ("Admission", "Admission"),
    )

    notice_id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    description = models.TextField()

    notice_date = models.DateField()

    expiry_date = models.DateField()

    attachment = models.FileField(
        upload_to="notice/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Active"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title