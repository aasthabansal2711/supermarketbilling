

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    @action(detail=False, methods=['get'])
    def category(self, request, *args, **kwargs):
        category = self.request.query_params.get('category', None)
        if category is not None:
            items = Item.objects.filter(category=category)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"category not provided"})
            
    @action(detail=False, methods=['get'])
    def subcategory(self, request, *args, **kwargs):
        subcategory = self.request.query_params.get('subcategory', None)
        if subcategory is not None:
            items = Item.objects.filter(subcategory=subcategory)
            serializer = self.get_serializer(items, many=True)
            return Response(serializer.data)
        else:
            return Response({"error":"subcategory not provided"})

class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemUpdateView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'