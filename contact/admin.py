from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','email','show', 
    ordering = '-id',
    list_filter ='created_date',
    list_per_page = 20
    list_max_show_all = 200
    list_display_links ='id','first_name',
    list_editable = 'show', 
    search_fields ='id','first_name','last_name','email', 

@admin.register(models.Category)
class CaregoryAdmin(admin.ModelAdmin):
    list_display='id','name'
    
