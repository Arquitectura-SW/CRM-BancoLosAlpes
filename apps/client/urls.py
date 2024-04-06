from django.urls import path
from apps.client.views import ClientAPICRUD
urlpatterns = [
    path('', ClientAPICRUD.as_view()),
]