from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Rebeca'}),
        label='Primeiro Nome',
        help_text='Digite Seu primeiro nome'
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Lohane'}),
        label='Sobrenome',
        
    )

    phone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'75988770024'}),
        label='Telefone',
        
    )

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder':'rebecaloh@email.com'}),
        label='Email',
        
    )
    picture = forms.ImageField(
        widget=forms.FileInput(attrs={'accept':'image/*'}),
    )


    # ATUALIZANDO O WIDGET
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'placeholder':'Perla Pepa'
    #     })

    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone','email','description','category','picture',)
        # CRIANDO UM NOVO widgets PARA O CAMPO
        # widgets= {'first_name': forms.TextInput(
        #     attrs={'placeholder':'Perla'}
        # )}

    def clean(self):

        cleaned_data = self.cleaned_data

        # self.add_error(
        #     None,
        #     ValidationError(
        #         'Mensagem error',
        #         code ='invalid'

        #     )
        # )
        return super().clean()

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Rebeca'}),
        label='Primeiro Nome',
        help_text='Digite Seu primeiro nome',
        required=True,
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Lohane'}),
        label='Primeiro Nome',
        help_text='Digite Seu primeiro nome'
    )

    
    email = forms.CharField(
        widget=forms.EmailInput(attrs={'placeholder':'rebecaloh@email.com'}),
        label='Email',
        
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'rebloh'}),
        label='Login',
        
    )
    class Meta:
        model = User
        fields=('first_name','last_name','email',
                'username','password1','password2')
        

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email',
                           ValidationError('Email já cadastrado',code='invalid'))
            return email
            
class Login(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'rebloh'}),
        label='Login',
        
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'rebloh'}),
        label='Login',
        
    )
    class Meta:
        model = User
        fields=('username','password',)
