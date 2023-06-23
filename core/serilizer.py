from .models import *
from rest_framework import serializers

class AtencionesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Atencion
        fields = '__all__'