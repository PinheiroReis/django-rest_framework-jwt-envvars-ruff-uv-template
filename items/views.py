from rest_framework import viewsets

from .models import Object, Category
from .serializers import ObjectSerializer, CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all().order_by("-date_joined")
    serializer_class = ObjectSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by("-created_at")
    serializer_class = CategorySerializer
