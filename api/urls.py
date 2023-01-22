#django imports
from django.urls import path, include
#rest frameworks imports
from rest_framework import routers
#views
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register('country', views.CountryViewSet, basename='country')
router.register('state', views.StateViewSet, basename="state")
router.register('city', views.CityViewSet, basename="city")
router.register('client', views.ClientViewSet, basename='client')
router.register('store', views.StoreViewSet, basename='store')


urlpatterns = [
    path('', include(router.urls))
]
