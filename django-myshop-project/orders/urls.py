from django.urls import path, include
from orders import views


urlpatterns = [
    path('', views.order_create, name='order_create'),
]