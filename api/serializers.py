
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import stock, articles,optionsStocks,investments


class stockApiSerializers(serializers.ModelSerializer):
     class Meta:
         model = stock
         fields = '__all__'

class articleApiSerializers(serializers.HyperlinkedModelSerializer):

    
    class Meta:
    
        model = articles
        fields = '__all__'
    readonly_fields = ('url', 'header_image')

class optionsApiSerializers(serializers.ModelSerializer):
     class Meta:
         model = optionsStocks
         fields = '__all__'

class investmentsApiSerializers(serializers.ModelSerializer):
     class Meta:
         model = investments
         fields = '__all__'
readonly_fields = ('url', 'header_image')
