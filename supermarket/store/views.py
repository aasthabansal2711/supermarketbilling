

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
    
    def get_queryset(self):
        queryset = Item.objects.all()
        category = self.request.query_params.get('category', None)
        subcategory = self.request.query_params.get('subcategory', None)
        if category is not None:
            queryset = queryset.filter(category=category)
        elif subcategory is not None:
            queryset = queryset.filter(subcategory=subcategory)
        return queryset

class ItemCreateView(CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemUpdateView(UpdateAPIView):                                        
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = 'id'