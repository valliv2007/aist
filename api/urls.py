from django.urls import include, path
from rest_framework import routers

from .views import CallBackViewSet, ProductViewSet, SubcategoryViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('subcategories', SubcategoryViewSet)
router.register('callbacks', CallBackViewSet)

urlpatterns = [
    path('', include(router.urls))
]
