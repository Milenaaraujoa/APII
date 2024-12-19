from django.contrib import admin
from django.urls import path, include
from cadastro_admin import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('redef_senha/', views.redef_senha, name='redef_senha'),
    path('senha/', views.senha, name='senha'),
    path('relatorio/', views.relatorio, name='relatorio'),
    path('eventos/', views.eventos, name='eventos'),
    path('turmas/', views.turmas, name='turmas'),  
]


