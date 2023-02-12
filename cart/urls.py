from django.urls import path


from . views import (
    cart_add, cart_add_in_cart,
    cart_detail,
    cart_remove
)


app_name = 'cart'

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('add_cart/<int:product_id>/', cart_add_in_cart, name='cart_add_in_cart'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
]
