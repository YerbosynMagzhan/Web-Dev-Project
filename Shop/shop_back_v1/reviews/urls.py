from django.urls import path
from .views import ReviewListAPIView, ReviewDetailAPIView

urlpatterns = [
    path('reviews/', ReviewListAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
]