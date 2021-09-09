
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import stock, articles,options,investments


class stockApiSerializers(serializers.ModelSerializer):
     class Meta:
         model = stock
         fields = '__all__'

class articleApiSerializers(serializers.HyperlinkedModelSerializer):

    
    class Meta:
    
        model = articles
        fields = (
        'title',
        'created_at',
        'header_image',
        'description',
        'description2'

    )
    readonly_fields = ('url', 'header_image')

class optionsApiSerializers(serializers.ModelSerializer):
     class Meta:
         model = options
         fields = '__all__'

class investmentsApiSerializers(serializers.ModelSerializer):
     class Meta:
         model = investments
         fields = '__all__'
readonly_fields = ('url', 'header_image')