from rest_framework import serializers
from .models import Foundation, ContentUpdate


class FoundationSerializer(serializers.HyperlinkedModelSerializer):
    contentupdates = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='contentupdate-detail'
    )

    class Meta:
        model = Foundation
        fields = ['id', 'name', 'description',
                  'headquarters_address', 'country', 'contentupdates']


class ContentUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContentUpdate
        fields = ['foundation', 'title', 'body']
