from django.urls import path
from contact import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    
]