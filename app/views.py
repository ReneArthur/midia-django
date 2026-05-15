from rest_framework import viewsets

from app.permissions import DjangoModelPermissionsComGet
from .models import Categoria, Episodio, Midia, Temporada
from .serializers import CategoriaSerializer, EpisodioSerializer, GroupSerializer, MidiaSerializer, PermissionSerializer, TemporadaSerializer, UserSerializer

from django.contrib.auth.models import User, Group, Permission

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsComGet]
    queryset = User.objects.prefetch_related("groups__permissions").prefetch_related("user_permissions").all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsComGet]
    queryset = Group.objects.prefetch_related("permissions").all()
    serializer_class = GroupSerializer


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [DjangoModelPermissionsComGet]
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class MidiaViewSet(viewsets.ModelViewSet):
    queryset = Midia.objects.all()
    serializer_class = MidiaSerializer


class TemporadaViewSet(viewsets.ModelViewSet):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer


class EpisodioViewSet(viewsets.ModelViewSet):
    queryset = Episodio.objects.all()
    serializer_class = EpisodioSerializer