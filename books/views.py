from django.shortcuts import render, get_object_or_404

from reviews.models import Review
from .models import Book

def book_list(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})