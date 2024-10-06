from rest_framework import generics
from .models import Category, Products, Cart, Checkout
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CheckoutSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class CategoryListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CheckoutCreateView(generics.CreateAPIView):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if not serializer.is_valid():
            return Response({
            "status" : False,
            "data" : serializer.errors
        })

        username = serializer.data['username']
        password = serializer.data['password']
        
        user_obj = authenticate(username = username, password = password)
        if user_obj:
            token , _ = Token.objects.get_or_create(user=user_obj)
            return Response({
                "status" : True,
                "data" : {'token' : str(token)}
        })
        return Response({
            "status" : True,
            "data" : {},
            "message" : "Invalid credentials"
        })