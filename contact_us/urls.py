from django.urls import path
from .views import MessageCreate


urlpatterns = [
    path('contactus/', MessageCreate.as_view(), name='contactus'),
]
