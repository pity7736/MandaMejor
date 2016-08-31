from rest_framework import serializers

from .models import Mandada


class MandadaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mandada
        fields = '__all__'
