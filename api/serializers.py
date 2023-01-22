#rest frameworks imports
from rest_framework import serializers
#model impoprts
from api.models import Country, Store, State, City, Client



class CountrySerializer(serializers.ModelSerializer):
    """ serializer for model Country """
    
    class Meta:
        model= Country
        fields = (
            'id',
            'name',
            'code'
        )
    
    # def validate(self, data):
    #     if data['nombre'] == '':
    #         raise serializers.ValidationError(
    #             "El campo nombre no puede estar vacio."
    #         )
    #     return data


class StateSerializer(serializers.ModelSerializer):
    """ Serializer for model State """

    country = CountrySerializer(many=False)


    class Meta:
        model= State
        fields = (
            'id',
            'name',
            'code',
            'country'
        )

class CitySerializer(serializers.ModelSerializer):
    """ Serializer for model City """

    state = StateSerializer(many=False)


    class Meta:
        model= City
        fields = (
            'id',
            'name',
            'code',
            'state'
        )
    
class StoreSerializer(serializers.ModelSerializer):
    """ serializer for model Store """
    
    class Meta:
        model= Store
        fields = (
            'id',
            'name',
            'code'
        )


class ClientSerializer(serializers.ModelSerializer):
    """ Serializer for model Client """

    country = CountrySerializer(many=False)
    state = StateSerializer(many=False)
    city = CitySerializer(many=False)
    favorite_store = StoreSerializer(many=False)


    class Meta:
        model= Client
        fields = (
            'id',
            'name',
            'sumame',
            'country',
            'state',
            'city',
            'favorite_store'
        )

