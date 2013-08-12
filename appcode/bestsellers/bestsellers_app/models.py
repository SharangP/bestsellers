from django.db import models


# Bestseller model
class Bestseller(models.Model):
    Title = models.TextField
    Author = models.CharField(max_length=255)
    Isbn = models.CharField(max_length=13)
    ImageUrl = models.URLField(max_length=255)
    BestsellerDate = models.DateField
    Rank = models.IntegerField(default=-1)
    BookList = models.ForeignKey('BookList')

    def __unicode__(self):
        return u"""
        < title:%s, author:%s, isbn:%s, imageurl:%s, bestsellerdate:%s, rank:%s, booklist:%s >
        """ % (self.Isbn, self.Title, self.Author, self.ImageUrl, self.BestsellerDate, self.Rank, self.BookList)


# BookList model
class BookList(models.Model):
    ListKey = models.SlugField
    DisplayName = models.CharField(max_length=255)

    def __unicode__(self):
        return u"""
        < listkey:%s, displayname:%s >
            """ % (self.ListKey, self.DisplayName)