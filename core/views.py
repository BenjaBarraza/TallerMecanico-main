from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserCreationForm,AtencionForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Categoria,Atencion
from django.contrib.auth.models import User
import json
import os
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .serilizer import AtencionesSerilizer


def index(request):
    categorias = list(Categoria.objects.all().values())   
    data={'categoria':categorias}
    return render(request, 'app/index.html',data)

def registro(request):
    data ={
        'form':CustomUserCreationForm()
    }
    categorias = list(Categoria.objects.all().values())
    data['categoria']=categorias
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Te has registrado correctamente")
        else:
            data['form']=CustomUserCreationForm()
            #messages.error(request, "Error ingrese los datos correctamente")
    return render(request, 'registration/registro.html', data)
    
def login(request):
    categorias = list(Categoria.objects.all().values())   
    data={'categoria':categorias}
    return render(request, 'registration/login.html',data)

def atenciones(request,id_mecanico):
    categorias = list(Categoria.objects.all().values())
    try:
        mecanico = User.objects.filter(id=id_mecanico)
        data = {
        'mecanico': mecanico[0]
        }
    except:
        return redirect(to=index)
    
    data['categoria']=categorias
    if request.method == 'POST':
        nombreCliente = request.POST.get('nombre-cliente')
        descripcion = request.POST.get('descripcion')
        categoria = request.POST.get('categoria')
        imagen = request.FILES['imagen']
        atencion=Atencion(mecanico_id=id_mecanico,nombreCliente=nombreCliente,Descripcion=descripcion,categoria_id=categoria,imagen=imagen)
        atencion.save()
    return render(request, 'app/atenciones.html',data)

def atencionesLista(request):
    atenciones = list(Atencion.objects.all().values())
    categorias = list(Categoria.objects.all().values())
    mecanicos = list(User.objects.all().values())
    data = {
        'atenciones':atenciones,
        'categoria':categorias,
        'mecanicos':mecanicos
        
    }
    return render(request,'app/atencionesLista.html',data)
def atencionModificar(request,id):
    atencion = get_object_or_404(Atencion, id=id)
    data = {
        'form':AtencionForm(instance=atencion)
    }
    if request.method == 'POST':
        formulario = AtencionForm(data=request.POST,instance=atencion, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Atencion modificada correctamente ")
            return redirect(to="atenciones_lsitado")
        else:
            data["form"] = formulario
            messages.warning(request, "ERROR: No se pudo modificar la atencion")

    return render(request,'app/atencionesModificar.html',data)

def atencionEliminar(request,id):
    atencion = get_object_or_404(Atencion, id=id)
    os.remove(os.getcwd()+'\\media\\'+str(atencion.imagen))
    atencion.delete()
    messages.success(request, "Atencion eliminada correctamente")
    return redirect(to="atenciones_lsitado")

def categoria(request,id):
    categ = list(Categoria.objects.filter(id=id).values())
    categorias = list(Categoria.objects.all().values())   
    data={'categoria':categorias,'categ':categ[0]}
    return render(request, 'app/categoria.html',data)


def cajacambio(request):
    categorias = list(Categoria.objects.all().values())   
    data={'categoria':categorias}
    return render(request, 'app/cajacambio.html',data)

def electroauto(request):
    categorias = list(Categoria.objects.all().values())   
    data={'categoria':categorias}
    return render(request, 'app/electroauto.html',data)

def servciogeneral(request):
    categorias = list(Categoria.objects.all().values())   
    data={'categoria':categorias}
    return render(request, 'app/servciogeneral.html',data)


def susydireccion(request):
    categorias = list(Categoria.objects.all().values())   
    data={'categoria':categorias}
    return render(request, 'app/susydireccion.html',data)


class AtecionesAPIView(APIView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request, id=None):
        if id is not None:
            listaAtecniones = Atencion.objects.filter(id=id).values()
            if len(listaAtecniones) > 0:
                atecion = listaAtecniones[0]
                return Response(atecion, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Atencion no encontrada'},status=status.HTTP_404_NOT_FOUND)
        else:
            atecion = Atencion.objects.all()
            serializer = AtencionesSerilizer(atecion, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
