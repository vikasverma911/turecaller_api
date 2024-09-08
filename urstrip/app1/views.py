from django.shortcuts import render
from .serailizers import ImageSerializer
from .models import Image
from rest_framework import generics, viewsets
# from rest_framework.response import Response
# from colorthief import ColorThief
# import matplotlib as plt

# Create your views here.


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     print()
    #     return self.create(request, *args, **kwargs)
