from django.urls import path, include
from autenticacao import views

# urls específicas do módulo de autenticação
urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('logar/', views.logar, name='logar'),
]
