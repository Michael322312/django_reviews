from django.urls import path

import reviews.views as reviews

urlpatterns = [
    path("", reviews.get_all_reviews)
] 