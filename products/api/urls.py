from django.urls import path
from .views import (ManufacturersView, ProductsView,
                    ManufacturerRetrieveView, 
                    UpdateManufacturerRetrieveView, 
                    DetailManufacturerRetrieveView,
                    CreateManufacturersView, 
                    DeleteManufacturersView,
                    products_exportpdf,
                    manufacturers_exportpdf)


urlpatterns = [
    

    path("products/", ProductsView.as_view(), name="product-list"),
    # path("products/<int:pk>/", product_detail, name="product-detail"),
    path('products/exportpdf/', products_exportpdf, name='export-pdf'),

    path("manufacturers/", ManufacturerRetrieveView.as_view(), name="manufacturer-list"),
    path("manufacturers/create", CreateManufacturersView.as_view(), name="manufacturer-create"),
    path("manufacturers/<int:pk>/edit/", UpdateManufacturerRetrieveView.as_view(), name="manufacturer-edit"),
    path("manufacturers/<int:pk>/", DetailManufacturerRetrieveView.as_view(), name="manufacturer-detail"),
    path("manufacturers/<int:pk>/delete/", DeleteManufacturersView.as_view(), name="manufacturer-delete"),
    path('manufacturers/exportpdf/', manufacturers_exportpdf, name='export-pdf'),


   
]