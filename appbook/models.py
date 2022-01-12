from django.db import models


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, max_length=150, verbose_name='Авторы')
    genres = models.ManyToManyField('Genre', max_length=150, verbose_name='Жанры')
    name = models.CharField(max_length=150, verbose_name='Название книги')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')


class Author(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название автора')


class Genre(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название жанра')
