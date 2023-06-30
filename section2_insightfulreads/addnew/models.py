from django.db import models

# Create your models here.

class Article(models.Model):
    article_name = models.CharField(max_length = 100)
    author_name = models.CharField(max_length = 100)
    publishing_date = models.DateField()
    category = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.article_name
    
    