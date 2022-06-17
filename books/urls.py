from django.urls import path
from.views import get_books, create_newBook,BookDetail,AuthorList,GenreList

urlpatterns = [

    path("",get_books, name="book-list"),
    path("create",create_newBook, name="book-create"),
    path("<int:pk>",BookDetail.as_view(),),
    path("author",AuthorList.as_view(), name="author"),
    path("genre",GenreList.as_view(), name = "genre"),  

]

   