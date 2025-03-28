"""clinic1402 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path , include
from django.contrib import admin
from django.conf.urls.static import static
from . import settings


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_app.urls')),
    path('cantact/', include('cantact_app.urls')),
    path('jobs/', include('jobs_app.urls')),
    path('reserv/', include('reserv_app.urls')),
    path('logout/', include('home_app.urls')),
    path('zib/', include('cash_app.urls')),
    path('it/', include('it_app.urls')),
    path('accountanc/', include('accountancy_app.urls')),
    path('sana/',include('accountancy_app.urls')),
    path('stor/', include('store_app.urls')),
    # path('image/', include('image_processing.urls')),
]

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
