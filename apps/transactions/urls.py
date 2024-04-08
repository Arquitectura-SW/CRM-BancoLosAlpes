from django.urls import path
from . import views

urlpatterns = [
    path('transactions/', views.transaction),
    path('transactions/<int:id>/', views.transaction_by_id),
]