"""haid_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers, permissions

from accounts.admin import *
from . import views

# 路由
router = routers.DefaultRouter()
router.register('api_info', views.APIInfoViewSet)
# router.register(r'users', views.UserViewSet, base_name='user')
# router.register(r'groups', views.GroupViewSet, base_name='group')

# 重要的是如下三行
# from rest_framework.schemas import get_schema_view
# from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title="工程API",
#         default_version='v1.0',
#         description="测试工程接口文档",
#         terms_of_service="https://www.notion.so/Roadmap-2-0-826f013eff1646eda4e52900738f8f57"
#     ),
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')),
    path('organization/', include('organization.urls')),
    path('project/', include('project.urls')),
    path('notification/', include('notification.urls')),
    path('oauth/', include('oauth.urls')),
    # url(r'', include('accounts.urls', namespace='account')),
    path('', views.index, name='index'),

    # 配置drf-yasg路由
    # path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
from django.contrib.staticfiles.urls import static
from haid_project import settings

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
