from rest_framework import serializers

from .models import List, Card


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = [
            'id', 'name'
        ]


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = [
            'id', 'title', 'description',
            'list', 'story_points', 'business_value'
        ]


