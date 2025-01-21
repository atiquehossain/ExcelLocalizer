from django.urls import path, re_path
from django.http import HttpResponseRedirect
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from core.views import HelloWorldView
from core.views import FlutterHomeCodeView
from django.contrib import admin  # Import the admin module


schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version="v1",
        description="API documentation for ExcelLocalizer",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', lambda request: HttpResponseRedirect('/swagger/')),  # Redirect root to Swagger UI
    path('admin/', admin.site.urls),
    path('hello/', HelloWorldView.as_view(), name='hello-world'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('flutter-home-code/', FlutterHomeCodeView.as_view(), name='flutter_home_code'),

]
