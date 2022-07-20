from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.user_signup_view),
    path('login/', views.user_login_view),
]