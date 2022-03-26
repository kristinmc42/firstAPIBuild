from unicodedata import name
from django.urls import include, path
from rest_framework import routers
from . import views

# a router works with a viewset to dynamically route requests
router = routers.DefaultRouter()
router.register(r"heroes", views.HeroViewSet)

# include login URLs for the browsable API

urlpatterns = [
  path("", include(router.urls)),
  path("api-auth/", include("rest_framework.urls", namespace="rest_framework"))
]