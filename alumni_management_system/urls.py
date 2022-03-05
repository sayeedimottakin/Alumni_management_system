"""alumni_management_system URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from home.views import home_view,discipline_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('home.urls')),
    # path('',home_view,name='home'),
    # path('discipline_view/',discipline_view,name='discipline_view'),
    path('alumni_profile/',include('alumni_profile.urls')),
    path('search/',include('search.urls')),
    path('social_media/',include('social_media.urls')),
    path('my_admin/',include('my_admin.urls')),
    path('admin/', admin.site.urls),
    path('events/',include('event.urls')),
    path('alumni_fee/',include('alumni_fee.urls')),
    path('news_letter/',include('news.urls')),
    path('accounts/', include('allauth.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)