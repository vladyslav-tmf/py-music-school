from django.urls import path, include
from rest_framework.routers import DefaultRouter
from musician.views import MusicianViewSet

router = DefaultRouter()
router.register("musicians", MusicianViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "musician"
