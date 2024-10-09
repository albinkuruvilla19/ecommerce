from rest_framework import generics
from .models import Category, Products, Cart, Checkout
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404

# class CategoryListCreateView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
    
@api_view(['GET','POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = CategorySerializer(category, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# class ProductListCreateView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

@api_view(['GET','POST'])
def product_list_create(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Products.objects.all()
#     serializer_class = ProductSerializer

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method in ['PUT', 'PATCH']:
        serializer = ProductSerializer(product, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# class CartListCreateView(generics.ListCreateAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cart_list_create(request):
    if request.method == 'GET':
        carts = Cart.objects.filter(user=request.user)
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@permission_classes([IsAuthenticated])
def cart_detail(request, pk):
    try:
        cart = Cart.objects.get(pk=pk, user=request.user)  
    except Cart.DoesNotExist:
        return Response({'error': 'Cart item not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method in ['PUT', 'PATCH']:
        serializer = CartSerializer(cart, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# class CheckoutCreateView(generics.CreateAPIView):
#     queryset = Checkout.objects.all()
#     serializer_class = CheckoutSerializer

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def checkout_create(request):
    if request.method == 'POST':
        serializer = CheckoutSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class LoginAPI(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = LoginSerializer(data=data)

#         if not serializer.is_valid():
#             return Response({
#             "status" : False,
#             "data" : serializer.errors
#         })

#         username = serializer.validated_data['username']
#         password = serializer.validated_data['password']
        
#         user_obj = authenticate(username = username, password = password)
#         if user_obj:
#             token , _ = Token.objects.get_or_create(user=user_obj)
#             return Response({
#                 "status" : True,
#                 "data" : {'token' : str(token)}
#         })
#         return Response({
#             "status" : True,
#             "data" : {},
#             "message" : "Invalid credentials"
#         })


@api_view(['POST'])
def login_api(request):
    data = request.data
    serializer = LoginSerializer(data=data)

    if not serializer.is_valid():
        return Response({
            "status": False,
            "data": serializer.errors
        }, status=400)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    
    user_obj = authenticate(username=username, password=password)
    if user_obj:
        token, _ = Token.objects.get_or_create(user=user_obj)
        return Response({
            "status": True,
            "data": {'token': str(token)}
        }, status=200)
    
    return Response({
        "status": False,
        "data": {},
        "message": "Invalid credentials"
    }, status=401)