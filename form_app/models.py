from django.db import models

class Book(models.Model):
    
    title = models.CharField(max_length=100, blank=False, db_column='title')
    description = models.TextField(db_column='description', max_length=1000)
    author = models.CharField(max_length=100, blank=False, db_column='author')
    year = models.IntegerField(default=2000, blank=False, db_column='year')


    def __str__(self):
        return self.title