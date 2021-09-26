from rest_framework.routers import DefaultRouter

from django.urls import path, include

from . import views

app_name = 'offers'

router=DefaultRouter()
router.register('offers', views.OfferViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
