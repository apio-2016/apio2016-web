"""apio2016_org URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views
import news.views

handler400 = views.bad_request
handler404 = views.page_not_found
handler500 = views.server_error

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^static/(?P<path>.*)$', views.static_serve),

    url(r'^$', news.views.news, name='main'),
    url(r'^results/$', views.results, name='results'),
    url(r'^about/$', views.about, name='about'),
    url(r'^schedules/$', views.schedules, name='schedules'),
    url(r'^regulations/$', views.regulations, name='regulations'),
    url(r'^competition/register/$', views.register, name='register'),
    url(r'^competition/call-for-tasks/$', views.callfortasks, name='callfortasks'),
    url(r'^competition/environment/$', views.environment, name='environment'),
    url(r'^competition/rules/$', views.rules, name='rules'),
    url(r'^host/$', views.host, name='host'),
    url(r'^links/$', views.links, name='links'),
]