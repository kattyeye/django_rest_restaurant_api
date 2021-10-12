from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('<int:pk>/', views.MenuDetailAPIView.as_view(), name="menu_detail"),
    path('', views.MenuListAPIView.as_view())
]
