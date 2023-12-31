"""
URL configuration for myproject project.

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
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('excelapp/', include('excelapp.urls')),  # Include app URLs here
    path('calculate/', include('cost_analysis.urls')), 
    path('',include('home.urls'))
]

if settings.DEBUG: # 只在开发环境中直接通过 Django 服务媒体文件
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.base_template = 'myproject/custom_admin_base.html'
admin.site.site_header = "洽兴报价管理系统"
admin.site.site_title = "洽兴报价管理系统"
admin.site.index_title = "欢迎使用洽兴报价管理系统"


