from django.urls import path

from plataforma import views

# urls específicas do módulo
urlpatterns = [
    path('', views.home, name="home"),
]
