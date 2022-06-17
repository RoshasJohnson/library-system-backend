from django.urls import path
from.views import get_books, create_newBook,BookDetail

urlpatterns = [

    path("",get_books, name="book-list"),
    path("create",create_newBook, name="book-create"),
    path("<int:pk>",BookDetail.as_view(),)
]

   