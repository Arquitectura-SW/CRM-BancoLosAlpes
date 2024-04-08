from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product),
    path('products/<int:id>/', views.product_by_id),
]