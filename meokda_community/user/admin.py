from django.contrib import admin
from .models import meokda_user


# Register your models here.
class MeokdaAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    

admin.site.register(meokda_user,MeokdaAdmin)
