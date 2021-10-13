from rest_framework import serializers

from .models import MenuItem


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('title', 'description', 'price', 'category')
