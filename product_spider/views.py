from rest_framework import viewsets, exceptions
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        try:
            return Product.objects.all()
        except Product.DoesNotExist:
            return exceptions.NotFound('No products found')
