from django.urls import path
from .views import * 

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('atenciones/', atenciones, name='atenciones'),
    path('auto1/', auto1, name='auto1'),
    path('auto2/', auto2, name='auto2'),
    path('auto3/', auto3, name='auto3'),
    path('auto4/', auto4, name='auto4'),
    path('auto5/', auto5, name='auto5'),
    path('auto6/', auto6, name='auto6'),
    path('cajacambio/', cajacambio, name='cajacambio'),
    path('electroauto/', electroauto, name='electroauto'),
    path('galeriafotos/', galeriafotos, name='galeriafotos'),
    path('mecanico1/', mecanico1, name='mecanico1'),
    path('mecanico2/', mecanico2, name='mecanico2'),
    path('mecanico3/', mecanico3, name='mecanico3'),
    path('mecanico4/', mecanico4, name='mecanico4'),
    path('mecanico5/', mecanico5, name='mecanico5'),
    path('mecanico6/', mecanico6, name='mecanico6'),
    path('mecanicos/', mecanicos, name='mecanicos'),
    path('servciogeneral/', servciogeneral, name='servciogeneral'),
    path('servicios/', servicios, name='servicios'),
    path('susydireccion/', susydireccion, name='susydireccion'),
    path('registro/', registro, name="registro"),
]
