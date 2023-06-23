from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria,Atencion

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
        widgets = {
            'email': forms.EmailInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese su correo',
                    'required':'required'
                }
            ),'first_name': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese su nombre',
                    'required':'required'
                }
            ),'last_name': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese su apellido',
                    'required':'required'
                }
            ),'username': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder':'Ingrese su usuario',
                    'required':'required'
                }
            ),
            }
class CategoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'

class AtencionForm(forms.ModelForm):

    class Meta:
        model = Atencion
        fields = '__all__'
