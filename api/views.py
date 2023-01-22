#rest framework
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from api import serializers, models


class CountryViewSet(viewsets.ModelViewSet):
    """ Endpoint for Country """
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer
    search_fields = ['name']


class StateViewSet(viewsets.ModelViewSet):
    """ Endpoint for State """
    serializer_class = serializers.StateSerializer
    queryset = models.State.objects.all()


class CityViewSet(viewsets.ModelViewSet):
    """ Endpoint for City """
    serializer_class = serializers.CitySerializer
    queryset = models.City.objects.all()


class ClientViewSet(viewsets.ModelViewSet):
    """ Endpoint for Client """
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    search_fields = ['name']


class StoreViewSet(viewsets.ModelViewSet):
    """ Endpoint for Store """
    queryset = models.Store.objects.all()
    serializer_class = serializers.StoreSerializer
    search_fields = ['name']

