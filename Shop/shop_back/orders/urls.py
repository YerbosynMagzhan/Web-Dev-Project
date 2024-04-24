from django.urls import path
from orders.views import OrderListAPIview, OrderDetailAPIview

urlpatterns = [
    path('orders/', OrderListAPIview.as_view()),
    path('orders/<int:pk>/', OrderDetailAPIview.as_view()),
]
