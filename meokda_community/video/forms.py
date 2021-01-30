from django import forms
from .models import Video
from user.models import meokda_user

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'restaurant',
            'foodname',
            'file',
            'price',
            'status',
            'distance',
        ]
