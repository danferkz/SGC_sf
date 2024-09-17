# capital/serializers.py
from rest_framework import serializers
from .models import Capital

class CapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capital
        fields = '__all__'
