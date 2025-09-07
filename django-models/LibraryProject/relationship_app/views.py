from django.shortcuts import render
from django.views.generic.detail import DetailView   # 👈 Explicit import
from .models import Book
from .models import Library   # 👈 Explicit import

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view: show library details + books
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
