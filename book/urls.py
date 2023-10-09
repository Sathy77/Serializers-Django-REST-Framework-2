from django.urls import path
from book.views import *

urlpatterns = [

    path('author-list/', authorlist, name='author-list'),
    path ('author-insert/', authorinsert, name='author-insert'),
    path ('author-update/<str:pk>/', authorupdate, name='author-update'),
    path ('author-delete/<str:pk>/', authorDelete, name='author-delete'),

    path('publisher-list/', publisherlist, name='publisher-list'),
    path ('publisher-insert/', publisherinsert, name='publisher-insert'),
    path ('publisher-update/<str:pk>/', publisherupdate, name= 'publisher-update'),

    path('booktype-list/', booktypelist, name='booktype-list'),
    path ('booktype-insert/', booktypeinsert, name='booktype-insert'),
    path ('bookType-update/<str:pk>/', bookTypeupdate, name= 'bookType-update'),

    path ('library-list/', librarylist, name='library-list'),
    path ('library-insert/', libraryinsert, name='library-insert'),
    path ('library-update/<str:pk>/', libraryupdate, name= 'library-update'),

    path ('book-list/', booklist, name='book-list'),
    path ('book-insert/', bookinsert, name='book-insert'), #problem
    path ('book-update/<str:pk>/', bookupdate, name= 'book-update'), #problem
    
    
    
    ]