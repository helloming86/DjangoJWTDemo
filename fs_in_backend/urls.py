"""fs_in_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', admin.site.urls),
    # 注册djangorestframework的路由
    # path(r'^api-auth', include('rest_framework.urls')),
    # restframework-jwt路由
    url(r'^api-token-auth', obtain_jwt_token),
]

# Django开发服务器在DEBUG=True的情况下会提供媒体文件服务
# static()方法仅用于开发环境
# 在生产环境中，不要用Django提供静态文件服务，而是用Web服务程序比如 nginx 等提供静态文件服务
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

