from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('<int:pk>/', views.MenuDetailAPIView.as_view(), name="book_detail"),
    path('', views.MenuListAPIView.as_view())
]
