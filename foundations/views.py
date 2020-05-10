from rest_framework import viewsets

from .models import Foundation, ContentUpdate
from .serializers import FoundationSerializer, ContentUpdateSerializer


class FoundationViewSet(viewsets.ModelViewSet):
    queryset = Foundation.objects.all().order_by('name')
    serializer_class = FoundationSerializer


class ContentUpdateViewSet(viewsets.ModelViewSet):
    queryset = ContentUpdate.objects.all()
    serializer_class = ContentUpdateSerializer
