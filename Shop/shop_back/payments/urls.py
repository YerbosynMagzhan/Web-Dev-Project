from django.urls import path
from .views import PaymentListAPIView, PaymentDetailAPIView

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view()),
    path('payments/<int:pk>/', PaymentDetailAPIView.as_view()),
]
