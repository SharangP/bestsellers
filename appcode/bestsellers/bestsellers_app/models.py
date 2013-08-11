from django.db import models


# Bestseller model
class Bestseller(models.Model):
    Title = models.TextField
    Author = models.CharField(max_length=255)
    Isbn = models.CharField(max_length=13)
    ImageUrl = models.URLField(max_length=255)
    Date = models.DateField
    Rank = models.IntegerField(default=-1)
    List = models.ForeignKey('BookList')


# BookList model
class BookList(models.Model):
    ListKey = models.SlugField
    DisplayName = models.CharField