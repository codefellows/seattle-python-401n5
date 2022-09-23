from rest_framework import serializers
from .models import Blog


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at', 'updated_at')
        model = Blog
