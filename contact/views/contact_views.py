from django.shortcuts import render
from contact.models import Contact

#app_name = 'contact'
contacts = Contact.objects.all()

context = {'contacts':contacts}
def index(request):
    return render(request,'contact/index.html',context)
