from rest_framework import generics
from menu.models import MenuItem
from .serializers import MenuSerializer
# Create your views here.


class MenuListAPIView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer
