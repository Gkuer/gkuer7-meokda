from django.urls import path
from . import views
from .models import Video

from django.conf.urls import url

app_name = 'video'

urlpatterns = [ 
    path('',views.VideoListView.as_view(), name='video_list'),
    path('new/', views.VideoCreateView.as_view(), name = 'video_new'),
    path('<int:pk>/',views.VideoDetailView.as_view(), name = 'video_detail'),
    path('<int:pk>/edit/',views.VideoDetailView.as_view(), name = 'video_edit'),
    path('<int:pk>/delete/',views.VideoDeleteView.as_view(), name = 'video_delete'),
    path('index/',views.index),
    path('test/',views.ArticlesView.as_view(), name='articles'),


]