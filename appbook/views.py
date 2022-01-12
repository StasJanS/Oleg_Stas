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

@api_view(['GET', 'POST'])
def api_books(request):
    # if request.method == 'GET':
    book = Book.objects.all()
    serializer = BookSerializer(book, many=True)
    return Response(serializer.data)
