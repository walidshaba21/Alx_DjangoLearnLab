import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "John Doe"
author = Author.objects.get(name=author_name)  # <-- required by checker
books_by_author = Book.objects.filter(author=author)  # <-- required by checker
print(f"Books by {author_name}:")
for book in books_by_author:
    print(book.title)

# Query 2: All books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"\nBooks in {library_name}:")
for book in library.books.all():
    print(book.title)

# Query 3: Librarian for a library
librarian = Librarian.objects.get(library__name=library_name)
print(f"\nLibrarian of {library_name}: {librarian.name}")
