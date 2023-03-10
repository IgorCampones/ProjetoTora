from django.urls import path
from . import views

#Caminhos criados, views contempla o direcionamento/ações e o nome do url para utilização
urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro', views.valida_cadastro, name='valida_cadastro'),
    path('valida_login', views.valida_login, name='valida_login'),
    path('home/', views.home, name='home'),
    path('sair/', views.sair, name='sair')
]
