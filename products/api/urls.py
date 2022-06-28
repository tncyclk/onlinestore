from django.urls import path
from .views import ManufacturersView, ProductsView, ManufacturerRetrieveView

urlpatterns = [
    

    path("products/", ProductsView.as_view(), name="product-list"),
    # path("products/<int:pk>/", product_detail, name="product-detail"),

    path("manufacturers/", ManufacturerRetrieveView.as_view(), name="manufacturer-list"),
    # path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer-detail")

   
]