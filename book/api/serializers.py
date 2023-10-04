from rest_framework import serializers
from book.models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields =['name', 'age', 'email']

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields =['name', 'campany', 'address']    

class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields =['type']   

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields =['name', 'address', 'email']           

class BookSerializer(serializers.ModelSerializer):
    booktype = BookTypeSerializer(many= False)
    author = AuthorSerializer(many= True)
    publisher = PublisherSerializer(many= True)
    library = LibrarySerializer(many= True)
    class Meta:
        model = Book
        fields =['book_name', 'booktype', 'author', 'publisher', 'library']               
