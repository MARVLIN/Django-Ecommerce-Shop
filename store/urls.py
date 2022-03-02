from django.urls import path

from . import views
from .views import ProductList, product_detail

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('items/', views.itemspage, name='items'),

    path('store/school_uniform/', views.school_uniform, name='school_uniform'),

    path('products', ProductList.as_view()),
    path('products/<int:pk>/', product_detail, name='product-detail')
]
