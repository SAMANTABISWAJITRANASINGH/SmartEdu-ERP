from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Book, BookIssue
from students.models import Student


# ==============================
# Book List
# ==============================

def book_list(request):

    search = request.GET.get("search")

    if search:

        books = Book.objects.filter(

            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(isbn__icontains=search) |
            Q(category__icontains=search)

        )

    else:

        books = Book.objects.all()

    return render(
        request,
        "library/book_list.html",
        {
            "books": books
        }
    )


# ==============================
# Add Book
# ==============================

def book_add(request):

    if request.method == "POST":

        Book.objects.create(

            title=request.POST.get("title"),

            author=request.POST.get("author"),

            publisher=request.POST.get("publisher"),

            isbn=request.POST.get("isbn"),

            category=request.POST.get("category"),

            edition=request.POST.get("edition"),

            total_copies=request.POST.get("total_copies"),

            available_copies=request.POST.get("available_copies"),

            cover=request.FILES.get("cover"),

            description=request.POST.get("description"),

        )

        return redirect("book_list")

    return render(request, "library/book_add.html")


# ==============================
# Book Profile
# ==============================

def book_profile(request, id):

    book = get_object_or_404(

        Book,

        book_id=id

    )

    return render(

        request,

        "library/book_profile.html",

        {

            "book": book

        }

    )


# ==============================
# Update Book
# ==============================

def book_update(request, id):

    book = get_object_or_404(

        Book,

        book_id=id

    )

    if request.method == "POST":

        book.title = request.POST.get("title")

        book.author = request.POST.get("author")

        book.publisher = request.POST.get("publisher")

        book.isbn = request.POST.get("isbn")

        book.category = request.POST.get("category")

        book.edition = request.POST.get("edition")

        book.total_copies = request.POST.get("total_copies")

        book.available_copies = request.POST.get("available_copies")

        book.description = request.POST.get("description")

        if request.FILES.get("cover"):

            book.cover = request.FILES.get("cover")

        book.save()

        return redirect("book_list")

    return render(

        request,

        "library/book_update.html",

        {

            "book": book

        }

    )


# ==============================
# Delete Book
# ==============================

def book_delete(request, id):

    book = get_object_or_404(

        Book,

        book_id=id

    )

    if request.method == "POST":

        book.delete()

        return redirect("book_list")

    return render(

        request,

        "library/book_delete.html",

        {

            "book": book

        }

    )


# ==============================
# Issue Book
# ==============================

def issue_book(request):

    students = Student.objects.all()

    books = Book.objects.filter(

        available_copies__gt=0

    )

    if request.method == "POST":

        student = get_object_or_404(

            Student,

            student_id=request.POST.get("student")

        )

        book = get_object_or_404(

            Book,

            book_id=request.POST.get("book")

        )

        BookIssue.objects.create(

            student=student,

            book=book,

            issue_date=request.POST.get("issue_date"),

            return_date=request.POST.get("return_date"),

            fine=request.POST.get("fine"),

            status=request.POST.get("status"),

            remarks=request.POST.get("remarks"),

        )

        book.available_copies -= 1

        book.save()

        return redirect("book_list")

    return render(

        request,

        "library/issue_book.html",

        {

            "students": students,

            "books": books

        }

    )


# ==============================
# Return Book
# ==============================

def return_book(request):

    students = Student.objects.all()

    books = Book.objects.all()

    if request.method == "POST":

        student = get_object_or_404(

            Student,

            student_id=request.POST.get("student")

        )

        book = get_object_or_404(

            Book,

            book_id=request.POST.get("book")

        )

        issue = BookIssue.objects.filter(

            student=student,

            book=book,

            status="Issued"

        ).first()

        if issue:

            issue.return_date = request.POST.get("return_date")

            issue.fine = request.POST.get("fine")

            issue.status = request.POST.get("status")

            issue.remarks = request.POST.get("remarks")

            issue.save()

            book.available_copies += 1

            book.save()

        return redirect("book_list")

    return render(

        request,

        "library/return_book.html",

        {

            "students": students,

            "books": books

        }

    )


# ==============================
# Library Report
# ==============================

def library_report(request):

    books = Book.objects.all()

    total_books = Book.objects.count()

    issued_books = BookIssue.objects.filter(

        status="Issued"

    ).count()

    returned_books = BookIssue.objects.filter(

        status="Returned"

    ).count()

    overdue_books = BookIssue.objects.filter(

        status="Late Return"

    ).count()

    return render(

        request,

        "library/library_report.html",

        {

            "books": books,

            "total_books": total_books,

            "issued_books": issued_books,

            "returned_books": returned_books,

            "overdue_books": overdue_books,

        }

    )