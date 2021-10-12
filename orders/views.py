from rest_framework import generics
from orders.models import Order
from .serializers import OrderSerializer
# Create your views here.


class OrderAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
