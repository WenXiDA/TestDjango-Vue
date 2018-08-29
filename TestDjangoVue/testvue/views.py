from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins

from .models import TestModel
from .serializers import TestModelSerializer

# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    max_page_size = 15


class TestModelListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer
    pagination_class = StandardResultsSetPagination