from django.db import models


# Create your models here.
class Book(models.Model):

    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned')
    ]
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('author.Author', related_name='books')
    publication_year = models.IntegerField()
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
