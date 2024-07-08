from django.shortcuts import render

#app_name = 'contact'

def index(request):
    return render(request,'contact/index.html')
