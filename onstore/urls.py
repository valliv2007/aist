
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('aistadmin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path('cart/', include('cart.urls', namespace='cart')),
        # path('paypal/', include('paypal.standard.ipn.urls')),
        # path('payment/', include('payment.urls', namespace='payment')),
        path('order/', include('orders.urls', namespace='orders')),
        path('cupons/', include('cupons.urls', namespace='cupon')),
        path('accounts/', include('django.contrib.auth.urls')),
        # path('users/', include('users.urls', namespace='users')),
        path('', include('lenivastore.urls'))
    ]
