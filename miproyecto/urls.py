from django.contrib import admin
from django.urls import path
from inicio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('estudios/', views.estudios, name='estudios'),
    path('contacto/', views.contacto, name='contacto'),
]

