from django.shortcuts import render,redirect
from django.contrib import messages,auth
from contact.forms import RegisterForm
from contact.forms import RegisteupdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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

def login_view(request):
        form = AuthenticationForm()

        if request.method == 'POST':
                form = AuthenticationForm(request,data=request.POST)
                if form.is_valid():
                        user = form.get_user()
                        auth.login(request,user)
                        messages.success(request,'Usuário logado!')
                        return redirect('contact:index')
                messages.error(request,'Dados não são válidos')
        context = {'form':form}
        return render(request,'contact/login.html',context)



@login_required(login_url='concact:login')
def user_update(request):
        if request.user.is_authenticated:
                form = RegisteupdateForm(instance=request.user)
                context ={'form':form}
                if request.method == 'POST':
                        form = RegisteupdateForm(data=request.POST,instance=request.user)
                        if form.is_valid():
                                form.save()
                                context ={'form':form}
                                return redirect('contact:user_update')
                        
                

                
                return render(request,'contact/user_update.html',context)
        else:
                messages.error(request,'Não existe usuário logado')
                return redirect('contact:login')
        
@login_required(login_url='concact:login')
def logout_view(request):
        auth.logout(request)
        return redirect('contact:login')