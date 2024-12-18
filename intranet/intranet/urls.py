from django.contrib import admin
from django.urls import path, include
from cadastro_admin import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login_user/', views.login_user, name='login_user'),
    path('accounts/', include('django.contrib.auth.urls')),
]

