from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'shop'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path(
        '<slug:categoria_slug>/',
        views.produto_list,
        name='produto_list_por_categoria'
    ),

    path('<int:id>/<slug:slug>/', views.produto_detalhe, name='produto_detalhe')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)