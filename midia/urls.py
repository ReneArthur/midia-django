from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import CategoriaViewSet, EpisodioViewSet, GroupViewSet, MidiaViewSet, PermissionViewSet, TemporadaViewSet, UserViewSet

router = DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('permissions', PermissionViewSet)

router.register('categorias', CategoriaViewSet)
router.register('midias', MidiaViewSet)
router.register('temporadas', TemporadaViewSet)
router.register('episodios', EpisodioViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]


