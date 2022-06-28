from .serializers import ManufacturerSerializer, ProductsSerializer, ManufacturerRetrieveSerializer
from products.models import Product, Manufacturer
from rest_framework.generics import ListAPIView


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ManufacturersView(ListAPIView):
    queryset = Manufacturer.objects.filter(active=True)
    serializer_class = ManufacturerSerializer

class ManufacturerRetrieveView(ListAPIView):
    queryset = Manufacturer.objects.filter(active=True)
    serializer_class = ManufacturerRetrieveSerializer
