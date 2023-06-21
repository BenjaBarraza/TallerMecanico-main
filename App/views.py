from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'registration/login.html')

def atenciones(request):
    return render(request, 'app/atenciones.html')

def auto1(request):
    return render(request, 'app/auto1.html')

def auto2(request):
    return render(request, 'app/auto2.html')

def auto3(request):
    return render(request, 'app/auto3.html')

def auto4(request):
    return render(request, 'app/auto4.html')

def auto5(request):
    return render(request, 'app/auto5.html')

def auto6(request):
    return render(request, 'app/auto6.html')

def cajacambio(request):
    return render(request, 'app/cajacambio.html')

def electroauto(request):
    return render(request, 'app/electroauto.html')

def galeriafotos(request):
    return render(request, 'app/galeriafotos.html')

def mecanico1(request):
    return render(request, 'app/mecanico1.html')

def mecanico2(request):
    return render(request, 'app/mecanico2.html')

def mecanico3(request):
    return render(request, 'app/mecanico3.html')

def mecanico4(request):
    return render(request, 'app/mecanico4.html')

def mecanico5(request):
    return render(request, 'app/mecanico5.html')

def mecanico6(request):
    return render(request, 'app/mecanico6.html')

def mecanicos(request):
    return render(request, 'app/mecanicos.html')

def servciogeneral(request):
    return render(request, 'app/servciogeneral.html')

def servicios(request):
    return render(request, 'app/servicios.html')

def susydireccion(request):
    return render(request, 'app/susydireccion.html')

def registro(request):
    data ={
        'form':CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to=index)
        else:
            data['form']=CustomUserCreationForm()
            #messages.error(request, "Error ingrese los datos correctamente")
    return render(request, 'registration/registro.html', data)