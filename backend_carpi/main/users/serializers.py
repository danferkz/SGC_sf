from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'password2', 'DNI', 'sexo', 'direccion', 'telefono']
        read_only_fields = []

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class ClientProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'DNI', 'sexo', 'direccion', 'telefono']  # Excluye password
        read_only_fields = [] # Ejemplo de campos que no deben ser editables
        

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])

    def validate_old_password(self, value):
        # Validamos si la contraseña antigua es correcta
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("La contraseña antigua no es correcta.")
        return value

    def validate(self, attrs):
        # Validamos que la nueva contraseña no sea igual a la antigua
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError({"new_password": "La nueva contraseña no puede ser igual a la antigua."})
        return attrs


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'password2']
        read_only_fields = []

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = CustomUser.objects.create_user(**validated_data)
        return user