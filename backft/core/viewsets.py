from rest_framework import viewsets

from .models import Frete
from .serializers import FreteSerializer

class FreteViewSet(viewsets.ModelViewSet):
    queryset = Frete.objects.all()
    serializer_class = FreteSerializer
    ordering_fields = '__all__'
    ordering = ('id')