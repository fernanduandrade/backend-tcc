from .models import Place, Category
from .serializers import PlaceSerializer, CategorySerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filterset_fields = ['title']
    filter_backends = [DjangoFilterBackend]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['category_name']
    filter_backends = [DjangoFilterBackend]