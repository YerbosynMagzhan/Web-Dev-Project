import json
from sneakers.models import Sneakers, Category
from sneakers.serializers import SneakersSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def sneakers_list(request):
    if request.method == 'GET':
        sneakers = Sneakers.objects.all()
        serializer = SneakersSerializer(sneakers, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = SneakersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sneakers_detail(request, id):
    try:
        sneakers = Sneakers.objects.get(id=id)
    except Sneakers.DoesNotExist as e:
        return Response({'error' : str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':    
        serializer = SneakersSerializer(sneakers)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = SneakersSerializer(
            instance=sneakers,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        sneakers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def sneakers_by_category(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return Response({'error' : str(e)}, status = status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        sneakers = Sneakers.objects.filter(category=category)
        serializer = SneakersSerializer(sneakers, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
