from django.shortcuts import render
from reviews.models import Review
# Create your views here.

def get_all_reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews_list": reviews
    }
    return render(
        request,
        "index.html",
        context
    )