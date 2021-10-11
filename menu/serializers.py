from rest_framework import serializers

from .models import MenuItem


class MenuSerializer(serializers.ModelSerializer):
    model = MenuItem
    fields = ('id', 'title', 'description', 'price')
