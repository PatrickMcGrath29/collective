from rest_framework import serializers
from .models import Foundation

class FoundationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Foundation
        fields = ('name', 'description', 'headquarters_address', 'country')
