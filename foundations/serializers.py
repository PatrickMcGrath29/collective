from rest_framework import serializers
from .models import Foundation, ContentUpdate

class FoundationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foundation
        fields = ['name', 'description', 'headquarters_address', 'country']

class ContentUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentUpdate
        fields = ['foundation', 'title', 'body']
