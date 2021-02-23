from .models import Catalogue, Book
from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import CreateOnlyDefault


class CatalogueSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Catalogue
        fields = ['id', 'name', 'description', 'created']

    
    def create(self, validated_data):
        catalogue = Catalogue.objects.create(**validated_data)
        return catalogue
        

class BookSerializer(serializers.ModelSerializer):
     
    catalogue_id = serializers.PrimaryKeyRelatedField(queryset = Catalogue.objects.all())
    
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'created','catalogue_id']
    
    def create(self, validated_data):
        book = Book.objects.create(**validated_data)
        return book      