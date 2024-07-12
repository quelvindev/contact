from django.shortcuts import render
from contact.models import Contact
from django.http import Http404
from django.db.models import Max
from django.shortcuts import get_object_or_404

#app_name = 'contact'

def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {
            'contacts':contacts,
            'site_title':'Contatos -'}

    return render(request,'contact/index.html',context)




def contact(request,contact_id):
    max_id = Contact.objects.aggregate(Max('id'))['id__max']
    
    #if (contact_id is None) or ( contact_id > max_id):
    #    raise Http404('Concato não existe')
    single_contact = get_object_or_404(Contact,pk=contact_id,show=True)
    
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '
    
    context ={
        'contact':single_contact,
        'site_title':contact_name
    
    }

    return render(request,'contact/contact.html',context)



def search(request):
    name = request.GET.get('q','').strip()

    print(name)
    contacts = Contact.objects.filter(show=True).order_by('-id')[:10]
    context = {
            'contacts':contacts,
            'site_title':'Contatos -'}

    return render(request,'contact/index.html',context)
