from functools import partial
from django.shortcuts import render

# Create your views here.

from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


from.serializers import BookSerializer, AuthorSerializer, GenreSerializer,BookDetailSerializer
from.models import Author, Book, Genre
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.

# gets all books records
@api_view(['GET'])
@permission_classes((AllowAny,))
def get_books(request):
        books = Book.objects.all()
        print(books, "books")
        serializer = BookDetailSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# creating a new book record
@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def create_newBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    get,update and  deleting a book record
    """
     
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404
 
    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookDetailSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
 
class AuthorList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    """
    list all authors and create a new author
    """
    def get(self, request):
        print("fetching all authors")
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        
        serializer = AuthorSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



  
class GenreList(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    """
    list all genres and create a new genre
    """

    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






