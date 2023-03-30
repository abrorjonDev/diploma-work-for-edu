from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_yasg import openapi

from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.documentation import include_docs_urls


schema_view = get_schema_view(
    openapi.Info(
        title="DOCUMENTATION",
        description="REST API",
        default_version="1.0.0",
        terms_of_service="ScienTech Solution",
        contact=openapi.Contact(email="admin@gmail.com"),
        license=openapi.License(name="Private"),
    ),
    public=False,
    permission_classes=(AllowAny, ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dj_rest_auth.urls')),
    path('openapi', schema_view.as_view(), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='drf-yasg/swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('', include(('edu.urls', 'edu'), namespace='edu'),),
    path('', include(('stats.urls', 'stats'), namespace='stats')),
    path('', include(('users.urls', 'users'), namespace='users')),

    ]
