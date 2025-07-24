from django.db import models
from books.models import Book

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.FloatField()
    review_text = models.TextField()
    review_date = models.DateField()

    def __str__(self):
        return f"Review for {self.book.title} by {self.reviewer_name}"