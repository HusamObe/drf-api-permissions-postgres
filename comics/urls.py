from django.urls import path
from .views import ComicListView, ComicDetailView

urlpatterns = [
   
    path('', ComicListView.as_view(), name= 'comic_list'),
    path('<int:pk>/',ComicDetailView.as_view(), name= 'comic_detail')
]