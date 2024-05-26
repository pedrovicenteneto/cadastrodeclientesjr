from django.urls import path
from app_cad_usuarios import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # rota, view responsável, nome de referência
    #login
    path('', views.login, name='login'),
    #logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # usuarios.com
    path('home/',views.home,name='home'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    # usuarios.com/editar_cliente
    path('editar_cliente/<int:id_usuario>', views.editar_cliente, name='editar_cliente')

]
