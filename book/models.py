from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100, null=False)
    campany = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.campany


class BookType(models.Model):
    type = models.CharField(max_length=100, null=False)   

    def __str__(self):
        return self.type 

class Library(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True) 

    def __str__(self):
        return self.name   

class Book(models.Model):
    book_name = models.CharField(max_length=100, null=False)
    booktype = models.ForeignKey(BookType, on_delete=models.SET_NULL, null=True)
    author = models.ManyToManyField(Author, blank=True, null=True)
    publisher = models.ManyToManyField(Publisher, blank=True, null=True)
    library = models.ManyToManyField(Library, null=True, blank=True)

    def __str__(self):
        return self.book_name

