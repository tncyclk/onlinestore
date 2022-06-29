from .serializers import ManufacturerSerializer, ProductsSerializer, ManufacturerRetrieveSerializer
from products.models import Product, Manufacturer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ManufacturersView(ListAPIView):
    queryset = Manufacturer.objects.filter(active=True)
    serializer_class = ManufacturerSerializer

class CreateManufacturersView(CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class ManufacturerRetrieveView(ListAPIView):
    queryset = Manufacturer.objects.filter(active=True)
    serializer_class = ManufacturerRetrieveSerializer


class UpdateManufacturerRetrieveView(RetrieveUpdateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class DetailManufacturerRetrieveView(RetrieveAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerRetrieveSerializer

class DeleteManufacturersView(DestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
