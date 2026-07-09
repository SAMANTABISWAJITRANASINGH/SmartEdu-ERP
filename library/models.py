from django.db import models
from students.models import Student


class Book(models.Model):

    CATEGORY_CHOICES = (
        ("Programming", "Programming"),
        ("Computer Science", "Computer Science"),
        ("Database", "Database"),
        ("Artificial Intelligence", "Artificial Intelligence"),
        ("Networking", "Networking"),
        ("Mathematics", "Mathematics"),
        ("Science", "Science"),
        ("Novel", "Novel"),
        ("General Knowledge", "General Knowledge"),
    )

    book_id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)

    author = models.CharField(max_length=100)

    publisher = models.CharField(max_length=100)

    isbn = models.CharField(max_length=30, unique=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    edition = models.CharField(max_length=50)

    total_copies = models.PositiveIntegerField()

    available_copies = models.PositiveIntegerField()

    cover = models.ImageField(
        upload_to="books/",
        blank=True,
        null=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class BookIssue(models.Model):

    STATUS_CHOICES = (
        ("Issued", "Issued"),
        ("Returned", "Returned"),
        ("Late Return", "Late Return"),
        ("Lost", "Lost"),
    )

    issue_id = models.AutoField(primary_key=True)

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )

    issue_date = models.DateField()

    return_date = models.DateField()

    fine = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Issued"
    )

    remarks = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.first_name} - {self.book.title}"