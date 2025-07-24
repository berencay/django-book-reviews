from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    published_date = models.DateField()
    description = models.TextField()
    cover_image = models.ImageField(upload_to="books/covers/", null=True, blank=True)

    def __str__(self):
        return self.title
