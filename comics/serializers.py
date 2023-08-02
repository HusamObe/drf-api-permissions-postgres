from rest_framework import serializers
from .models import Comic

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        # fields = '__all__'
        fields =['owner', 'title', 'desc']
        