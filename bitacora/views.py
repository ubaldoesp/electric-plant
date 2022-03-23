from django.http import Http404
import django_filters.rest_framework
from django.db.models import Sum
from bitacora.models import Bitacora
from .serializer import BitacoraSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework import status


class BitacoraView(ListCreateAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer
   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BitacoraDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    


class BitacoraEnergyView(ModelViewSet):
    queryset = Bitacora.objects.all()
    serializer_class = BitacoraSerializer
    
    # def get_queryset(self):
    #     dispositivo = self.request.query_params.get('id_dispositivo')
    #     return Bitacora.objects.filter(dispositivo__startswith=dispositivo)
  

    # def get_sum(self):
    #     dispositivo = self.request.query_params.get('id_dispositivo')
    #     print('*******************')
    #     potencia_sum = self.get_queryset().aggregate(Sum("potencia"))["potencia__sum"]
    #     return Response({"id_dispositivo": dispositivo, "energia": potencia_sum})

