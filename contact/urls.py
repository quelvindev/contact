from django.urls import path
from contact import views

app_name ="contact"

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('search/', views.search,name="search"),

    # CRUD
    path('contact/create', views.create,name="create"),
    path('contact/<int:contact_id>/detail', views.contact,name="contact"),
    
    
]