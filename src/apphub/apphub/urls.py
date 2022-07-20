"""apphub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages import views as page_views

from users import views as user_views
from softwares import views as software_views

urlpatterns = [
    path('', page_views.home_page_view, name='home'),
    path('auth/', include('users.urls')),
    path('home/', page_views.home_page_view, name='pages_home'),
    path('software/', software_views.software_page_view, name='software_page'),
    # path('search/', software_views.software_search_view, name='search_view'),
    path('publish-software/', software_views.publish_software_view, name='publish_software'),
    # path('login/', page_views.login_view, name='login'),
    path('login/', user_views.user_login_view, name='user_login'),
    path('signup/', user_views.user_signup_view, name='user_signup'),
    path('logout/', user_views.user_logout_view, name='user_logout'),
    path('test/', page_views.test_page_view, name='test_page'),
    path('admin/', admin.site.urls),
]
