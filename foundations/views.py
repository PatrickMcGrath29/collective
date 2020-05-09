from rest_framework import viewsets

from .models import Foundation
from .serializers import FoundationSerializer

class FoundationViewSet(viewsets.ModelViewSet):
    queryset = Foundation.objects.all().order_by('name')
    serializer_class = FoundationSerializer
