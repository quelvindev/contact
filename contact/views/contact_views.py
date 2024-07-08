from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
from django.db.models import Max

#app_name = 'contact'

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {'contacts':contacts}

    return render(request,'contact/index.html',context)




def contact(request,contact_id):
    max_id = Contact.objects.aggregate(Max('id'))['id__max']
    
    if (contact_id is None) or ( contact_id > max_id):
        raise Http404('Concato não existe')
    single_contact = Contact.objects.get(pk=contact_id)
    
    context ={
        'contact':single_contact,
    
    }

    return render(request,'contact/contact.html',context)
