from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import CategoriaViewSet, MidiaViewSet

router = DefaultRouter(trailing_slash=False)
router.register('categorias', CategoriaViewSet)
router.register('midias', MidiaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]


