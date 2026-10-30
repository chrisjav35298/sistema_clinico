from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', include('pacientes.urls')),
    path('especialidades/', include('especialidades.urls')),
    path('servicios/', include('servicios.urls')),
    path('medicos/', include('medicos.urls')),
    path('admin/', admin.site.urls),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),name='logout'),
]