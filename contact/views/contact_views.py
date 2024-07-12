from django.shortcuts import render,get_object_or_404,redirect
from contact.models import Contact
from django.db.models import Q
from django.http import Http404
from django.db.models import Max


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
    search_value = request.GET.get('q','').strip()
    if search_value == '':
        return redirect('contact:index')
    
    contacts = Contact.objects.filter(show=True)\
                                .filter(
                                    Q(first_name__icontains=search_value) |
                                    Q(last_name__icontains=search_value) |
                                    Q(phone__icontains=search_value) |
                                    Q(email__icontains=search_value)
                                    )\
                                .order_by('-id')
    context = {
            'contacts':contacts,
            'site_title':'Contatos -'}

    return render(request,'contact/index.html',context)
