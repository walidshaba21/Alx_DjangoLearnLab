# 📚 CRUD Operations for Book Model in Django

This document demonstrates how to use Django’s ORM (Object-Relational Mapper) to perform basic **Create**, **Retrieve**, **Update**, and **Delete** (CRUD) operations on the `Book` model from the `bookshelf` app.

Each operation is performed using the Django shell (`python manage.py shell`) and includes both the Python commands used and the expected output.

---

## ✅ Create a Book

We will create a book with the title `"1984"`, author `"George Orwell"`, and publication year `1949`.

```python
# Import the Book model
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Print the object
book

# Output
<Book: 1984>

# Retrieve the book by its ID (assuming it's the only book so far)
retrieved_book = Book.objects.get(id=book.id)

# Print book details
print(retrieved_book.title)
print(retrieved_book.author)
print(retrieved_book.publication_year)


# Output
1984
George Orwell
1949


# Update the book's title
retrieved_book.title = "Nineteen Eighty-Four"

# Save the updated book
retrieved_book.save()

# Confirm the update
updated_book = Book.objects.get(id=retrieved_book.id)
print(updated_book.title)

# Output
Nineteen Eighty-Four

# Delete the book
updated_book.delete()

# Output
(1, {'bookshelf.Book': 1})

# Check if any books are left
Book.objects.all()

# Output
<QuerySet []>