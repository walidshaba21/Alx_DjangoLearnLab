Step 1: Creation of 'bookshelf' app within 'LibraryProject' project

Step 2: Defining the Book model in 'bookshelf/models.py with required field requested

Step 3: Set up the app with the projects properly by adding the app in the projects setting (INSTALLED_APPS) and also configuring the database properly using mysql

Step 4: Migrate the project properly using 'makemigrations' and 'migrate'


Step 5: Interacted with the Model via Django Shell for basic CRUD works

Step 6: Documenting the project in the README.md file

NB: Below is my terminal's Output

./LibraryProject/__pycache__:
total 32
drwxr-xr-x@ 6 musashaba  staff   192 Mar 23 21:31 .
drwxr-xr-x@ 8 musashaba  staff   256 Mar 23 21:31 ..
-rw-r--r--@ 1 musashaba  staff   194 Mar 23 21:31 __init__.cpython-314.pyc
-rw-r--r--@ 1 musashaba  staff  2503 Mar 23 21:31 settings.cpython-314.pyc
-rw-r--r--@ 1 musashaba  staff  1063 Mar 23 21:31 urls.cpython-314.pyc
-rw-r--r--@ 1 musashaba  staff   691 Mar 23 21:31 wsgi.cpython-314.pyc
➜  LibraryProject git:(main) ✗ clear
➜  LibraryProject git:(main) ✗ python manage.py startapp bookshelf
➜  LibraryProject git:(main) ✗ python manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
bookshelf.Book.author: (fields.E120) CharFields must define a 'max_length' attribute.
bookshelf.Book.title: (fields.E120) CharFields must define a 'max_length' attribute.
➜  LibraryProject git:(main) ✗ python manage.py makemigrations
Migrations for 'bookshelf':
  bookshelf/migrations/0001_initial.py
    + Create model Book
➜  LibraryProject git:(main) ✗ python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, bookshelf, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying bookshelf.0001_initial... OK
  Applying sessions.0001_initial... OK
➜  LibraryProject git:(main) ✗ python manage.py shell
13 objects imported automatically (use -v 2 for details).

Cmd click to launch VS Code Native REPL
Python 3.14.3 (main, Feb  3 2026, 15:32:20) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> product = Product.objects.create(
... title="Rich dad Poor Dad",
... author="Robert Kiyosaki",
... publication_year=1997
... )
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Product' is not defined
>>> product = Product.objects.create(
... )
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'Product' is not defined
>>> book= Book.objects.create(
... title="Rich dad Poor Dad",
... author="Robert Kiyosaki",
... publication_year=1997
... )
>>> Book.objects.all()
<QuerySet [<Book: Book object (1)>]>
>>> quit()
now exiting InteractiveConsole...
➜  LibraryProject git:(main) ✗ python manage.py makemigrations
No changes detected
➜  LibraryProject git:(main) ✗ python manage.py migrate       
Operations to perform:
  Apply all migrations: admin, auth, bookshelf, contenttypes, sessions
Running migrations:
  No migrations to apply.
➜  LibraryProject git:(main) ✗ python manage.py shell         
13 objects imported automatically (use -v 2 for details).

Cmd click to launch VS Code Native REPL
Python 3.14.3 (main, Feb  3 2026, 15:32:20) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from bookshelf.models import Book
>>> 
>>> book = Book.objects.create(
...     title="Clean Code",
...     author="Uncle Bob",
...     publication_year=2008,
... )
>>> Book.objects.all()
<QuerySet [<Book: Rich dad Poor Dad>, <Book: Clean Code>]>
>>> Book.objects.get(id=1)
<Book: Rich dad Poor Dad>
>>> Book.objects.get(id=2)
<Book: Clean Code>
>>> book = Book.Objects.get(id=1)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'Book' has no attribute 'Objects'. Did you mean: 'objects'?
>>> book = Book.objects.get(id=1)
>>> object.title = "Poor Dad Rich Dad"
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: cannot set 'title' attribute of immutable type 'object'
>>> book.title = "Poor Dad Rich Dad"
>>> book.save()
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> book.save()
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> book.object.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Book' object has no attribute 'object'. Did you mean: 'objects'?
>>> book.objects.all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/opt/homebrew/lib/python3.14/site-packages/django/db/models/manager.py", line 186, in __get__
    raise AttributeError(
        "Manager isn't accessible via %s instances" % cls.__name__
    )
AttributeError: Manager isn't accessible via Book instances
>>> Book.objects.all()
<QuerySet [<Book: Clean Code>]>
>>> 
