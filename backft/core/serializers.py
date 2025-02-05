from rest_framework import serializers
from .models import Frete

class FreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frete
        fields = '__all__'