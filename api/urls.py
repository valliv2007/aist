from django.urls import include, path
from rest_framework import routers

from .views import CallBackViewSet,  CuponViewSet, ProductViewSet, SubcategoryViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('subcategories', SubcategoryViewSet)
router.register('callbacks', CallBackViewSet)
router.register('cupons', CuponViewSet)

urlpatterns = [
    path('', include(router.urls))
]
