from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user),
    path('register/', views.register),
    path('logout/', views.logout_user),
    path('getUserData/', views.get_user_data),
]
