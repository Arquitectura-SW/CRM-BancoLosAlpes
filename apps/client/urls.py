from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client),
    path('clients/<int:id>/', views.client_by_id),
]