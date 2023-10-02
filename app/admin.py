from django.contrib import admin
from .models import Contact,Profile_Picture
# Register your models here.

@admin.register(Contact)
class Contact_Register(admin.ModelAdmin):
    list_display =  ['id','name','email','message']

@admin.register(Profile_Picture)
class PP_Register(admin.ModelAdmin):
    list_display = ['id','image']
