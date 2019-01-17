"""terra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from knox import views as knox_views
from rest_framework import routers

from projects.views import LoginView, ExampleView

router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^auth/login/', LoginView.as_view(), name='knox_login'),
    url(r'^auth/logout/',
        knox_views.LogoutView.as_view(),
        name='knox_logout'),
    url(r'^auth/logoutall/',
        knox_views.LogoutAllView.as_view(),
        name='knox_logoutall'),
    url(r'^example', ExampleView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
