from django.urls import path

from .views import all_book, api_books

urlpatterns = [
    path('', all_book, name='all_book'),
    path('api/', api_books)


]