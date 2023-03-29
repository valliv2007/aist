from django.urls import include, path
from rest_framework import routers

from .views import ProductViewSet, SubcategoryViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('subcategories', SubcategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
