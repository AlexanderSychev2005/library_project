from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author', related_name='books')
    publication_year = models.IntegerField()
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.title
