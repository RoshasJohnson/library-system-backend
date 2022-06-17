from rest_framework import serializers
from.models import Book, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = "__all__"

        


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"




class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = "__all__"


class BookDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        depth = 1
        fields = "__all__"
