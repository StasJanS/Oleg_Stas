from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


def all_book(request):
    book = Book.objects.all()

    context = {
        'book': book,
    }
    return render(request, 'appbook/all_book.html', context)


@api_view(['GET'])  # выводит все книги с полным описанием на странице
def api_books(request):
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)


@api_view(['GET'])  # выводит по id одну книгу с полным описанием на странице
def api_books_detail(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)
