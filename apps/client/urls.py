from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

"""urlpatterns = [
    path('clients/', views.ClientAPICRUD.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)"""
urlpatterns = [
    path('clients/', views.client),
    path('clients/<int:id>/', views.client_by_id),
]