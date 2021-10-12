from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('<int:pk>/', views.OrderDetailAPIView.as_view(), name = 'order_detail' ),
    path('', views.OrderAPIView.as_view()),
]