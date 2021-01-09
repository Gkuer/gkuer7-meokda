from django.contrib import admin
from .models import board
# Register your models here.
class boardadmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(board,boardadmin)