from django.urls import path
from .views import landingview, supplierlistview, addsupplier, deletesupplier, productlistview, addproduct, deleteproduct, edit_supplier_get, edit_supplier_post, edit_product_get, edit_product_post, products_filtered

urlpatterns = [
    # suppliers
    path('', landingview),
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
    

    # Products
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),
]
