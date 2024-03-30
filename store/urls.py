from django.urls import path
from rest_framework.authtoken import views as auth_view
from .views import StoreView, CategoryView, CategoryDetailView, StoreCreateStore, ProductView, AllProductsView, AllCategoriesView, CategoryProductsView, ProductSearchView
from . import views


urlpatterns = [
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:product_id>/', ProductView.as_view(), name='product-detail'),
    path('all-products/', AllProductsView.as_view(), name='all-products'),
    path('all-categories/', AllCategoriesView.as_view(), name='all-categories'),
    path('category-products/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),
    path('search-products/', ProductSearchView.as_view(), name='product-search'),
    path('stores/', StoreView.as_view(), name='store-list'),
    path('stores/<int:store_id>/', StoreView.as_view(), name='store-detail'),
    path('categories/', CategoryView.as_view(), name='category'),
    path('categories/<int:category_id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('stores/create/', StoreCreateStore.as_view(), name='store-list'),


    


]