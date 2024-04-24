from django.urls import path
from sneakers import views

urlpatterns = [
    path('sneakers/', views.sneakers_list),
    path('sneakers/<int:id>/', views.sneakers_detail),
    path('category/<int:id>/sneakers/', views.sneakers_by_category),
]
