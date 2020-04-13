from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',auth_view.LoginView.as_view(template_name='account/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='account/logout.html'),name='logout'),
]
