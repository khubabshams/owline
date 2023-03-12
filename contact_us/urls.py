from django.urls import path
from .views import MessageCreate, MessageList, MessageDetail


urlpatterns = [
    path('contactus/', MessageCreate.as_view(), name='contactus'),

    path('inbox', MessageList.as_view(), name='inbox'),
    path('inbox/<pk>/', MessageDetail.as_view(),
         name='message_details'),
]
