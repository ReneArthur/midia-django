from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers
from .models import Categoria, Episodio, Midia, Temporada 




# Usuários e Grupos

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

    permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True,
    )

    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    # groups = GroupSerializer(many=True, read_only=True)
    user_permissions = serializers.PrimaryKeyRelatedField(
        queryset=Permission.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = User
        fields = ("id", "username", "password", "email", "is_staff", "groups", "user_permissions")

    # A gente precisa sobrescrever o create e o update para a senha ser criptografada corretamente.
    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)

        user.set_password(password)
        user.save()

        return user

    
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        instance = super().update(instance, validated_data)

        if password:
            instance.set_password(password)
            instance.save()

        return instance

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['groups'] = GroupSerializer(instance.groups, many=True).data
    #     return representation

# Modelos do sistema

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class MidiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Midia
        fields = ('id', 'nome', 'descricao', 'data_criacao', 'categorias', 'tipo', 'created_at', 'updated_at')
        # read_only_fields = ('exemplo')

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = '__all__'

class EpisodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodio
        fields = '__all__'