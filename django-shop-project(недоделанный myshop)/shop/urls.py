from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # ex: /shop/
    path('', views.index, name='index'),
    # ex: /shop/product-slug/
    path('<str:slug>/', views.detail, name='detail'),
]
