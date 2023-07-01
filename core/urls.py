from django.urls import path
from .views import * 

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('atenciones/<id_mecanico>', atenciones, name='atenciones'),
    path('atenciones_listado/',atencionesLista , name='atenciones_lsitado'),
    path('atencionModificar/<id>',atencionModificar , name='atencionModificar'),
    path('eliminaratecnion/<id>/',atencionEliminar, name='eliminaratecnion'),
    path('categoria/<id>', categoria, name='categoria'),
    path('cajacambio/', cajacambio, name='cajacambio'),
    path('electroauto/', electroauto, name='electroauto'),
    path('servciogeneral/', servciogeneral, name='servciogeneral'),
    path('susydireccion/', susydireccion, name='susydireccion'),
    path('registro/', registro, name="registro"),
    path('atencionesAPI/', AtecionesAPIView.as_view(), name='atencionesAPI'),
    path('atencionesAPI/<int:id>', AtecionesAPIView.as_view(), name='atencionAPI_id'),
]
