from django.contrib import admin

# Register your models here.
from book.models import *

admin.site.register({Author, Publisher, BookType, Library, Book})
