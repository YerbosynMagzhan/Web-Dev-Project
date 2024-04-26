from django.urls import path
from .views import CartItemListCreateView, CartItemRetrieveUpdateDestroyView, CartListCreateView, CartRetrieveUpdateDestroyView

urlpatterns = [
    path('cart-items/', CartItemListCreateView.as_view(), name='cart-item-list-create'),
    path('cart-items/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view(), name='cart-item-retrieve-update-destroy'),
    path('carts/', CartListCreateView.as_view(), name='cart-list-create'),
    path('carts/<int:pk>/', CartRetrieveUpdateDestroyView.as_view(), name='cart-retrieve-update-destroy'),
]