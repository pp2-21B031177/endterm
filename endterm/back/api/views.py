from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, ProductSerializer, CreditCardSerializer, CartSerializer
from .models import Product, CreditCard, Cart, User

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CreditCardListView(generics.ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class CreditCardDetailView(generics.RetrieveAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

class CartList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer