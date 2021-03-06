from django.urls import path, include


app_name = 'api_v1'


urlpatterns = [
    path('orders/', include('orders.urls', namespace="orders")),
    path('menu-items/', include('menu.urls', namespace='menu')),
]
