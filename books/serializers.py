from rest_framework import serializers
from.models import  Book   , Author , Genre


class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Author
        fields = ('url', 'first_name', 'last_name', 'pen_name')


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        depth = 1
        fields = ('id', 'title', 'description', 'author', 'genre')




class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('id', 'name')