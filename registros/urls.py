from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from registros import views

routers = routers.DefaultRouter()
routers.register(r'registros', views.RegistroView,'registros')
routers.register(r'categorias', views.CategoriaView,'categorias')


urlpatterns = [
    path('api/v1/', include(routers.urls)),
    path('docs', include_docs_urls(title='Registros API')),

]
