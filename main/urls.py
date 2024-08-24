
from django.urls import path, include
from .views import webhook

urlpatterns = [
    path('webhook', webhook, name='webhook'),
]
