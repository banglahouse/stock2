
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import stock, articles


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