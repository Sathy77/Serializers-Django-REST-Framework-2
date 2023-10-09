from rest_framework import serializers
from book.models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields ='__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields ='__all__'   

class BookTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookType
        fields ='__all__'    

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields ='__all__'          

class BookSerializer(serializers.ModelSerializer): #for POST in serializer we only use ID for foreign key.
    booktype = BookTypeSerializer(many= False) 
    author = AuthorSerializer(many= True)
    publisher = PublisherSerializer(many= True)
    library = LibrarySerializer(many= True)
    class Meta:
        model = Book
        fields ='__all__' 