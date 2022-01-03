from django.urls import path
from . import views

urlpatterns = [
    path('admin/order/', views.orderWine, name='orderWine'),
]