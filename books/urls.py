from django.urls import path
from.views import get_books, create_newBook

urlpatterns = [

    path("",get_books, name="book-list"),
    path("create",create_newBook, name="book-create"),
]

