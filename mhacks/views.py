from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Query
from .serializer import QuerySerializer

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
