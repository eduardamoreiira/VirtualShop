from django.contrib import admin
from django.urls import include, path
from django.config import settings
from django.config import static


urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('shop.urls',namespace='shop')),
]

if settings.DEBUG:
    urlpatterns+=static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )