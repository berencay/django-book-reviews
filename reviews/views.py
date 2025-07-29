from django.shortcuts import render, get_object_or_404
from .models import Review

def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, "books/review_detail.html", {'review': review})

# Create your views here.
