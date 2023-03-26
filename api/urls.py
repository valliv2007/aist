from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
