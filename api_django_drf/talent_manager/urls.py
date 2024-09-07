"""talent_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.http import HttpResponse

schema_view = get_schema_view(
    openapi.Info(
        title="Talent Manager API",
        default_version='v1',
        description="Manager talent API Swagger",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contato@empresa.com"),
        # license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],
)
def home(request):
    return HttpResponse("wellcome to talent manager API!, you need access the swagger  http://localhost:8000/swagger")

urlpatterns = [
      path('', home),  # Define a URL raiz
    path('admin/', admin.site.urls),
    path('api/', include('candidates.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]