from re import search
from .models import Place, Category
from .serializers import PlaceSerializer, CategorySerializer
from rest_framework import viewsets, filters


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    search_fields = ['tilte']
    filter_backend = (filters.SearchFilters)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['category_name']
    filter_backend = (filters.SearchFilters)