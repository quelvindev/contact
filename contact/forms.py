from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from contact.models import Contact


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



    # ATUALIZANDO O WIDGET
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields['first_name'].widget.attrs.update({
    #         'placeholder':'Perla Pepa'
    #     })

    class Meta:
        model = Contact
        fields = ('first_name','last_name','phone','email','description','category')
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
