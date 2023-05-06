from django.urls import path
from .views import UserCreateView, ProductDetailView, ProductListView, CreditCardListView, CreditCardDetailView, CartList, CartDetail

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('credit-cards/', CreditCardListView.as_view(), name='credit-card-list'),
    path('credit-cards/<int:pk>/', CreditCardDetailView.as_view(), name='credit-card-detail'),
    path('carts/', CartList.as_view()),
    path('carts/<int:pk>/', CartDetail.as_view()),
]