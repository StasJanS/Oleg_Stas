from django.urls import path

from .views import all_book, api_books, api_books_detail

urlpatterns = [
    path('', all_book, name='all_book'),
    path('api/', api_books),
    path('api/<int:id>', api_books_detail),


]