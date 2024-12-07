from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/',admin.site.urls),
    path('account/', include('acoount.urls', namespace='account')),
    path('cart/', include('cart.urls',namespace='cart')),
    path('', include('shop.urls',namespace='shop')),
]

if settings.DEBUG:
    urlpatterns+=static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
