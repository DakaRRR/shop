from .models import Product
from .serializers import ProductSerializer
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.parsers import MultiPartParser, FormParser


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.order_by('price')
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)

    filter_backends = [DjangoFilterBackend, filters.SearchFilter,]
    filterset_fields = ['status']
    search_fields = ['title', 'sku']
