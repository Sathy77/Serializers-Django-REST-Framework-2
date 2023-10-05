from django.shortcuts import render
from book.models import *
from book.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import *

@api_view(['GET'])
def authorlist(request):
	author = Author.objects.all()
	authorserializer = AuthorSerializer(author, many=True)
	return Response(authorserializer.data)

@api_view(['GET'])
def publisherlist(request):
	publisher = Publisher.objects.all()
	puthoraerializer = PublisherSerializer(publisher, many=True)
	return Response(puthoraerializer.data)

@api_view(['GET'])
def booktypelist(request):
	booktype = BookType.objects.all()
	bookTypeserializer = BookTypeSerializer(booktype, many=True)
	return Response(bookTypeserializer.data)

@api_view(['GET'])
def librarylist(request):
	library = Library.objects.all()
	libraryserializer = LibrarySerializer(library, many=True)
	return Response(libraryserializer.data)

@api_view(['GET'])
def booklist(request):
	book = Book.objects.all()
	bookserializer = BookSerializer(book, many=True)
	return Response(bookserializer.data)


@api_view(['POST'])
def authorinsert(request):
	serializer = AuthorSerializer(data= request.data)

	if serializer.is_valid():
		serializer.save()

	return Response("serializer.data")

@api_view(['POST'])
def authorupdate(request, pk):
	author = Author.objects.get(id=pk)
	serializer = AuthorSerializer(instance= author, data= request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def authorDelete(request, pk):
	author = Author.objects.get(id=pk)
	author.delete

	return Response("Deleted Author")
	

