"""
URL configuration for modelproject5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home_view),
    path('all/',views.model_view),
    path("add/",views.add_view),
    path("home/",views.main_page_view),
    path("java/",views.java_views),
    path("python/",views.python_views),
    path("aptitude/",views.aptitude_views),
    path("accounts/",include('django.contrib.auth.urls')),
    path("logout/",views.logout_view),
    path("signup/",views.signup_view)

]
