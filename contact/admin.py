from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','frist_name','last_name','email', 
    ordering = '-id',
    list_filter ='created_date',
    list_per_page = 20
    list_max_show_all = 200
    list_display_links ='id','frist_name',
    search_fields ='id','frist_name','last_name','email', 
    
