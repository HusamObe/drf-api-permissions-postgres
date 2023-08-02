from django.shortcuts import render
from .models import Comic
from rest_framework.generics import ListAPIView, RetrieveAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import ComicSerializer
from .permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class ComicListView(ListCreateAPIView):

    queryset = Comic.objects.all()
    serializer_class = ComicSerializer


class ComicDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

