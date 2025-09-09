from django.urls import path
from .views import index, create_invoice, send_message, add_customer

urlpatterns = [
    path('', index, name='index'),
    path('add_customer/', add_customer, name='add_customer'),
    path('create_invoice/', create_invoice, name='create_invoice'),
    path('send_message/', send_message, name='send_message')
]