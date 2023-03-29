from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from ..userApp import views as user_views

app_name = "userApp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),

    path("register", user_views.register_request, name="register"),
    path("login", user_views.login_request, name="login"),
    path("logout", user_views.logout_request, name="logout"),
]
