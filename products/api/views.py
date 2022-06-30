from itertools import product
from .serializers import ManufacturerSerializer, ProductsSerializer, ManufacturerRetrieveSerializer
from products.models import Product, Manufacturer
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView

from django.http import HttpResponse
from rest_framework.decorators import api_view
import tempfile
from weasyprint import HTML
from django.template.loader import render_to_string
import datetime


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


@api_view(['GET'])
def products_exportpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' attachment; filename=Products' + \
                                      str(datetime.datetime.now()) + '.pdf'
    
    response['Content-Transfer-Encoding'] = 'binary'
    products = Product.objects.all()
    html_string = render_to_string('products/product.html', {'products': products})
    html = HTML(string=html_string)
    result = html.write_pdf()
    
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        
        output = open(output.name, 'rb')
        response.write(output.read())
        
    return response

@api_view(['GET'])
def manufacturers_exportpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = ' attachment; filename=Manufacturer' + \
                                      str(datetime.datetime.now()) + '.pdf'
    
    response['Content-Transfer-Encoding'] = 'binary'
    manufacturers = Manufacturer.objects.all()
    html_string = render_to_string('manufacturers/manufacturer.html', {'manufacturers': manufacturers})
    html = HTML(string=html_string)
    result = html.write_pdf()
    
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        
        output = open(output.name, 'rb')
        response.write(output.read())
        
    return response
