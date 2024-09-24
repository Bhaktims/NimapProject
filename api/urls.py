from django.urls import include, path
from api.views import ClientViewSet,ProjectViewSet
from rest_framework import routers 


router = routers.DefaultRouter()
router.register(r'clients',ClientViewSet)
router.register(r'projects',ProjectViewSet)

urlpatterns = [
    path('',include(router.urls))
    
]