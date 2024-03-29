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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import SimpleRouter

from projects.views import (
    ConfirmProjectInvitationView, ContactView, FileUploadView, FileViewSet,
    LayerViewSet, MapViewSet, ProjectInvitationTokenViewSet, ProjectViewSet,
    TestAuthView, TestErrorView, UserViewSet)
from quotations.views import RequestViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'files', FileViewSet)
router.register(r'layers', LayerViewSet)
router.register(r'maps', MapViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'projects/invitations', ProjectInvitationTokenViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Terra API',
        default_version='v1',
        description='This is the description of the API',
        terms_of_service='https://www.dymaxionlabs.com/terms/',
        contact=openapi.Contact(email='contact@dymaxionlabs.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny, ),
)

urlpatterns = [
    # Documentation
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    url(r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),

    # Authentication
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),

    # Administration
    url(r'^admin/', admin.site.urls),

    # Other custom views
    url(r'^projects/invitations/(?P<key>[^/]+)/confirm/?',
        ConfirmProjectInvitationView.as_view()),
    url(r'^contact/?', ContactView.as_view()),
    url(r'^files/upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),

    # Test views
    url(r'^test/auth/?', TestAuthView.as_view()),
    url(r'^test/error/?', TestErrorView.as_view()),

    # ...
    url(r'^', include(router.urls)),
]

urlpatterns += [path('admin/django-rq/', include('django_rq.urls'))]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
