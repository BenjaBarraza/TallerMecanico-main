from django import forms
from .models import  Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
