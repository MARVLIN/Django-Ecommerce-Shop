from django.urls import path

from . import views
from .views import product_detail, category_detail, SearchResultsView

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),


    path('<slug:category_slug>/<slug:slug>/', product_detail, name='product-detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),

    path('search', SearchResultsView.as_view(), name='search_results'),

]
