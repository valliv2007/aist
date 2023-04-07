from django.urls import include, path
from rest_framework import routers

from .views import CallBackViewSet,  CuponViewSet, OrderViewSet, OrderItemViewSet, ProductViewSet, SubcategoryViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('subcategories', SubcategoryViewSet)
router.register('callbacks', CallBackViewSet)
router.register('cupons', CuponViewSet)
router.register('orders', OrderViewSet)
router.register('ordersitems', OrderItemViewSet)

urlpatterns = [
    path('', include(router.urls))
]
