from django.urls import path
from book.views import *

urlpatterns = [

    path('author-list/', authorlist, name='author-list'),
    path('publisher-list/', publisherlist, name='publisher-list'),
    path('booktype-list/', booktypelist, name='booktype-list'),
    path ('library-list/', librarylist, name='library-list'),
    path ('book-list/', booklist, name='book-list'),
    ]