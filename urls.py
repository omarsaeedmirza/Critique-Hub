from .views import MovieViewSet, RatingViewSet, UserViewSet
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import include
router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
