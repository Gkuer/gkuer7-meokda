from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.views.generic import ListView, DeleteView, DetailView,CreateView,UpdateView 
# Create your views here.


class VideoListView(ListView):
    model = Video

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'form.html'

class VideoDetailView(DetailView):
    model = Video


class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = 'form.html'


class VideoDeleteView(DeleteView):
    model = Video