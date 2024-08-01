from django.shortcuts import render,redirect
from django.contrib import messages
from contact.forms import RegisterForm
from contact.forms import Login

def register(request):
        form = RegisterForm()

        # messages.info(request,'Mensagem Informativa')
        # messages.success(request,'Mensagem Sucesso!')
        # messages.error(request,'Mensagem Erro!')
        # messages.warning(request,'Mensagem Alerta!')

        if request.method == 'POST':
                form = RegisterForm(request.POST)
                if form.is_valid():
                        form.save()
                        messages.success(request,'Usuário cadastrado !')
                        return redirect('contact:index')

        
                



        context = {
            'form':form
            }

        return render(request,'contact/register.html',context)

def login(request):
        form = Login()
        context = {'form':form}
        return render(request,'contact/login.html',context)