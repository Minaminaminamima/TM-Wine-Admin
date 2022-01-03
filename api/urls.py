from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('order', views.order, name="order"),
    path('order/<int:order_num>/', views.btn_click, name="btn_click"),
    path('storage', views.storage, name="storage"),
    #path('order', views.orderWine, name='orderWine'),
]