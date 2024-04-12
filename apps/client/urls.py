from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.client),
    path('clients/<str:id_or_id_number>/', views.client_by_id_number),
]
